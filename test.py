import cvxpy as cp
import numpy as np
from scipy.spatial import ConvexHull
from shapely.geometry import Polygon
from shapely.affinity import scale
import matplotlib.pyplot as plt

def svm_q3_modified(A, B):

    m = A.shape[1]
    k = B.shape[1]
    n = A.shape[0]

    w = cp.Variable(n)
    gamma = cp.Variable(2)

    constraints = [
        w.T @ B[:, j] >= gamma[0] for j in range(k)
    ] + [
        w.T @ A[:, i] <= gamma[1] for i in range(m)
    ] + [
        gamma[0] == gamma[1] + 1
    ]

    objective = cp.Minimize(cp.norm(w, 2))
    problem = cp.Problem(objective, constraints)
    problem.solve()

    return w.value, gamma.value


# Generate a random midpoint with x and y being independent
mid_point = np.random.rand(2) * 20 - 10

# Generate example data for class +1
A = np.random.rand(2, 20) * 5  - np.array([[np.random.randint(-15, 15)], [np.random.randint(-15, 15)]])

# Generate example data for class -1
B = np.random.rand(2, 20) * 5 + np.array([[np.random.randint(-15, 15)], [np.random.randint(-15, 15)]])

# Calculate w and gamma with the modified function
w, gamma = svm_q3_modified(A, B)
print("w:", w)
print("gamma:", gamma)
print("distance:", np.abs(gamma[1]-gamma[0]) / np.linalg.norm(w))

# Scatter plot of the data points
plt.scatter(A[0, :], A[1, :], color='blue', label='+1')
plt.scatter(B[0, :], B[1, :], color='red', label='-1')

# Calculate hyperplane
x = np.linspace(-20, 20, 100)  # Adjust range to extend hyperplanes
y1 = (-w[0] * x + gamma[0]) / w[1]  # Solve for y
y2 = (-w[0] * x + gamma[1]) / w[1]  # Solve for y

# Plot the hyperplane
plt.plot(x, y1, color='red', label='Hyperplane, alpha = {gamma[0]}'.format(gamma=gamma))
plt.plot(x, y2, color='blue', label='Hyperplane, beta = {gamma[1]}'.format(gamma=gamma))

# Calculate convex hull for class +1
hull1 = ConvexHull(A.T)
for simplex in hull1.simplices:
    plt.plot(A[0, simplex], A[1, simplex], 'k-')
plt.fill(A[0, hull1.vertices], A[1, hull1.vertices], 'blue', alpha=0.3)

# Calculate convex hull for class -1
hull2 = ConvexHull(B.T)
for simplex in hull2.simplices:
    plt.plot(B[0, simplex], B[1, simplex], 'k-')
plt.fill(B[0, hull2.vertices], B[1, hull2.vertices], 'red', alpha=0.3)

# Set plot limits
plt.xlim(-20, 20)
plt.ylim(-20, 20)

# Add labels and legend
plt.xlabel("x1")
plt.ylabel("x2")
plt.legend()
plt.title("SVM Q3 Solution")

# Show the plot
plt.grid(True)
# plt.show()
# Define the variables
x1 = cp.Variable()
x2 = cp.Variable()

# Define the objective function
objective = cp.Minimize(0.5 * (x1 - 3)**2 + 0.5 * (x2 + 3)**2)

# Define the constraints
constraints = [
    x1 + 2 * x2 >= 0,
    x1**2 + x2**2 <= 1
]

# Formulate the problem
problem = cp.Problem(objective, constraints)

# Solve the problem
problem.solve()
# Get the Lagrange multipliers (dual values)
lambda_values = [constraint.dual_value for constraint in constraints]

# Print the Lagrange multipliers
print("Lagrange multipliers:", lambda_values)
# Calculate the Lagrangian value
# Calculate the Lagrangian value
lagrangian_value = 0.5 * (x1.value - 3)**2 + 0.5 * (x2.value + 3)**2 - lambda_values[0] * (x1.value + 2 * x2.value) + lambda_values[1] * (x1.value**2 + x2.value**2 - 1)

# Calculate the gradient of the Lagrangian
lagrangian_gradient = np.array([
    x1.value - 3 - lambda_values[0] + 2 * lambda_values[1] * x1.value,
    x2.value + 3 - 2 * lambda_values[0] + 2 * lambda_values[1] * x2.value
])

# Print the gradient of the Lagrangian
print("Gradient of the Lagrangian:", lagrangian_gradient)

# Print the Lagrangian value
print("Lagrangian value:", lagrangian_value)
# Print the results
print("Optimal value of x1:", x1.value)
print("Optimal value of x2:", x2.value)
print("Optimal objective value:", problem.value)