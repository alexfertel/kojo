#!/usr/bin/python3
import numpy as np
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt

from analysis.means import sample

def plot():
    x_val = [x for x in np.arange(0, 1, .05)]
    y_val = [y for y in np.arange(60, 30 * 20, 30)]
    z_val = [sample(y, x) for x in x_val for y in y_val]

    print(len(x_val))
    print(len(y_val))
    print(len(z_val))

    fig = plt.figure()
    # plt.plot3D(x_val, y_val, z_val)

    ax = plt.axes(projection='3d')
    ax.scatter3D(x_val, y_val, z_val)
    plt.show()

if __name__ == "__main__":
    plot()

