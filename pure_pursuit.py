# A code to track an input path using pure pursuit algorithm
# the input is a series of (x, y) points that represent the path
# the output is the steering angle that the car should take to follow the path
# the final output is the path that the car took using bicycle model and steering angles from pure pursuit

import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import distance
import math
import matplotlib.patches as patches


# define the car model
class Car:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.theta = 0
        self.delta = 0
        self.L = 2.9
        self.velocity = 1
        self.dt = 0.1

    def update(self, delta):
        self.x = self.x + self.velocity * np.cos(self.theta) * self.dt
        self.y = self.y + self.velocity * np.sin(self.theta) * self.dt
        self.theta = self.theta + self.velocity / self.L * np.tan(delta) * self.dt
        self.delta = delta

    def plot(self):
        plt.plot(self.x, self.y, 'ro')
        plt.plot([self.x, self.x + 0.5*np.cos(self.theta)], [self.y, self.y + 0.5*np.sin(self.theta)], 'r-')
        rect = patches.Rectangle((self.x - 0.5, self.y - 0.25), 1, 0.5, angle=math.degrees(self.theta), edgecolor='r', facecolor='none')
        plt.gca().add_patch(rect)


class PurePursuit:
    def __init__(self, path, Lfc):
        self.path = path
        self.Lfc = Lfc
        self.goal = [path[-1][0], path[-1][1]]

    def find_target_index(self, car):
        # find the target point on the path that the car should follow
        # the target point is the point on the path that is Lfc ahead of the car

        # find the closest point on the path to the car
        min_dist = float('inf')
        min_ind = 0
        for i in range(len(self.path)):
            d = distance.euclidean([car.x, car.y], self.path[i])
            if d < min_dist:
                min_dist = d
                min_ind = i

        print("The car location is: ", [car.x, car.y])
        print("The closest point on the path to the car is: ", self.path[min_ind])
        # find the target point that is Lfc ahead of the car
        Lf = self.Lfc
        while Lf > 0 and min_ind + 1 < len(self.path):
            dx = self.path[min_ind + 1][0] - self.path[min_ind][0]
            dy = self.path[min_ind + 1][1] - self.path[min_ind][1]
            L = np.sqrt(dx**2 + dy**2)
            Lf -= L
            min_ind += 1

        print("The target point is (Lfc): ", self.path[min_ind])
        return min_ind

    def pure_pursuit_control(self, car, target_ind):
        # find the steering angle that the car should take to follow the path
        # the steering angle is calculated based on the target point on the path

        # find the target point
        tx = self.path[target_ind][0]
        ty = self.path[target_ind][1]

        # find the angle between the car and the target point
        alpha = math.atan2(ty - car.y, tx - car.x) - car.theta

        # find the steering angle
        Lf = self.Lfc
        delta = math.atan2(2.0 * car.L * np.sin(alpha) / Lf, 1.0)

        return delta

    def plot(self):
        path = np.array(self.path)
        plt.plot(path[:, 0], path[:, 1], 'b-')


def main():
    # define the path that the car should follow
    path = [[0, 0], [0, 5], [0,10], [5, 10], [10, 10]]

    # define the car and the pure pursuit controller
    car = Car()
    pure_pursuit = PurePursuit(path, 0.1)

    # simulate the car following the path
    for i in range(200):
        # check if the car reached the goal
        d = distance.euclidean([car.x, car.y], pure_pursuit.goal)
        if d < 0.1:
            print("The car reached the goal at iteration: ", i)
            break
        target_ind = pure_pursuit.find_target_index(car)
        delta = pure_pursuit.pure_pursuit_control(car, target_ind)
        car.update(delta)
        car.plot()

    # plot the path that the car should follow
    pure_pursuit.plot()

    plt.axis('equal')
    plt.grid(True)
    plt.show()

if __name__ == '__main__':
    main()
