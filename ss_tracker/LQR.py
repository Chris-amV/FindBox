"""
3D Control of Quadcopter
based on https://github.com/juanmed/quadrotor_sim/blob/master/3D_Quadrotor/3D_control_with_body_drag.py
The dynamics is from pp. 17, Eq. (2.22). https://www.kth.se/polopoly_fs/1.588039.1550155544!/Thesis%20KTH%20-%20Francesco%20Sabatino.pdf
"""
from ss_tracker import nonlinear_dynamics
import numpy as np
import scipy
from scipy.integrate import odeint
from .nonlinear_dynamics import g, m, Ix, Iy, Iz


def u(x, _t):
    # the controller
    dis = _t - t
    dis[dis < 0] = np.inf
    idx = dis.argmin()
    UX = Ks[0].dot(np.array([signalx[idx], 0, 0, 0]) - x[[0, 1, 8, 9]])[0]
    UY = Ks[1].dot(np.array([signaly[idx], 0, 0, 0]) - x[[2, 3, 6, 7]])[0]
    UZ = Ks[2].dot(np.array([signalz[idx], 0]) - x[[4, 5]])[0]
    UYaw = Ks[3].dot(np.array([signalyaw[idx], 0]) - x[[10, 11]])[0]
    return np.array([UZ, UY, UX, UYaw])


def cl_nonlinear(x, t, u):
    x = np.array(x)
    dot_x = nonlinear_dynamics.f(x, u(x, t) + np.array([m * g, 0, 0, 0]))
    return dot_x


def lqr(A, B, Q, R):
    """Solve the continuous time lqr controller.
    dx/dt = A x + B u
    cost = integral x.T*Q*x + u.T*R*u
    """
    # http://www.mwm.im/lqr-controllers-with-python/
    # ref Bertsekas, p.151

    # first, try to solve the ricatti equation
    X = np.matrix(scipy.linalg.solve_continuous_are(A, B, Q, R))

    # compute the LQR gain
    K = np.matrix(scipy.linalg.inv(R) * (B.T * X))

    eigVals, eigVecs = scipy.linalg.eig(A - B * K)

    return np.asarray(K), np.asarray(X), np.asarray(eigVals)


# The control can be done in a decentralized style
# The linearized system is divided into four decoupled subsystems

# X-subsystem
# The state variables are x, dot_x, pitch, dot_pitch
Ax = np.array(
    [
        [0.0, 1.0, 0.0, 0.0],
        [0.0, 0.0, g, 0.0],
        [0.0, 0.0, 0.0, 1.0],
        [0.0, 0.0, 0.0, 0.0],
    ]
)
Bx = np.array([[0.0], [0.0], [0.0], [1 / Ix]])

# Y-subsystem
# The state variables are y, dot_y, roll, dot_roll
Ay = np.array(
    [
        [0.0, 1.0, 0.0, 0.0],
        [0.0, 0.0, -g, 0.0],
        [0.0, 0.0, 0.0, 1.0],
        [0.0, 0.0, 0.0, 0.0],
    ]
)
By = np.array([[0.0], [0.0], [0.0], [1 / Iy]])

# Z-subsystem
# The state variables are z, dot_z
Az = np.array([[0.0, 1.0], [0.0, 0.0]])
Bz = np.array([[0.0], [1 / m]])

# Yaw-subsystem
# The state variables are yaw, dot_yaw
Ayaw = np.array([[0.0, 1.0], [0.0, 0.0]])
Byaw = np.array([[0.0], [1 / Iz]])

####################### solve LQR #######################
Ks = []  # feedback gain matrices K for each subsystem
for A, B in ((Ax, Bx), (Ay, By), (Az, Bz), (Ayaw, Byaw)):
    n = A.shape[0]
    m = B.shape[1]
    Q = np.eye(n)
    Q[0, 0] = 10.0  # The first state variable is the one we care about.
    R = np.diag(
        [
            1.0,
        ]
    )
    K, _, _ = lqr(A, B, Q, R)
    print(K)
    Ks.append(K)

######################## simulate #######################
# time instants for simulation


def LQR(sx, sy, sz, Tf, steps, phi0=0.0, theta0=0.0, psi0=0.0):
    global signalx, signaly, signalz, t, signalyaw
    signalx, signaly, signalz = sx, sy, sz
    t_max = Tf
    t = np.linspace(0, Tf, steps)
    num_w = len(signalx)
    X0 = np.zeros(12)
    X0[0] = sx[0]
    X0[2] = sy[0]
    X0[4] = sz[0]
    X0[6] = phi0  # roll
    X0[8] = theta0  # pitch
    X0[10] = psi0  # yaw

    signalyaw = np.zeros_like(signalz)  # we do not care about yaw
    # simulate
    x_nl = odeint(cl_nonlinear, X0, t, args=(u,))

    return x_nl
