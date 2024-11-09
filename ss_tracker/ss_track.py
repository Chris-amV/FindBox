import numpy as np
from .LQR import LQR
from .trajectoryGen import trajectoryGenie
import matplotlib.pyplot as plt


# Define the class ss_track to track just a single variable
# Remaining variables are calculated by trajectoryGemerator
# Track a given 1D signal
# The signal is a 1D numpy array as input to the class
# the time is total time of the signal.


# The id is id of state variable from 1 to 12: [x, y, z, vx, vy, vz, phi, theta, psi, p, q, r]
# id is assumed 1 for now so x is the only input signal
class ss_track:
    def __init__(self, signal, time=10):
        self.signal = signal
        # Define the duration:
        self.t_f = time  # in seconds
        self.num_points = len(signal)
        self.time = np.linspace(0, self.t_f, self.num_points)

    def trajectory(self):
        # Define the trajectory starting state:
        pos0 = [0, 0, 0]  # position
        vel0 = [0, 0, 0]  # velocity
        acc0 = [0, 0, 0]  # acceleration

        # Define the goal state:
        self.posf = [pos0[0] + self.t_f, pos0[1], pos0[2] + 30]  # position
        self.velf = [0, 0, 0]  # velocity
        self.accf = [0, 9.81, 0]  # acceleration

        # Rapid trajectory generator
        self.px, self.py, self.pz = trajectoryGenie(
            pos0, vel0, acc0, self.posf, self.velf, self.accf, self.t_f, self.num_points
        )
        x_nl = LQR(self.signal, self.py, self.pz, self.t_f + 2, self.num_points)
        self.ax, self.ay, self.az = x_nl[:, 0], x_nl[:, 2], x_nl[:, 4]
        # self.roll, self.pitch, self.yaw = x_nl[:, 6], x_nl[:, 8], x_nl[:, 10]
        x_nlF = []
        for i in x_nl:
            x_nlF.append(i[0])
        return x_nlF

    def plot_whole_trajectory(self):
        # plot the px, py, pz trajectory as reference TRAJECTORY IN 3d
        # And ax, ay, az as the actual trajectory in 3d in same plot
        fig = plt.figure()
        ax = fig.add_subplot(111, projection="3d")
        ax.plot(self.signal, self.py, self.pz, label="Reference")
        ax.plot(self.ax, self.ay, self.az, label="Actual")
        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.set_zlabel("Z")
        ax.legend()
        plt.show()

    def plot_signal(self):
        # plot the signal
        plt.plot(self.time, self.signal, label="Original Signal")
        # plot the tracking as ax
        plt.plot(self.time, self.ax, label="Tracking result")
        plt.xlabel("Time")
        plt.ylabel("Signal")
        plt.legend()
        plt.show()


def main():

    pass


if __name__ == "__main__":
    main()
