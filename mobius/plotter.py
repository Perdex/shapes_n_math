import math
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np


def set_axes_equal(ax):
    '''Make axes of 3D plot have equal scale so that spheres appear as spheres,
    cubes as cubes, etc..  This is one possible solution to Matplotlib's
    ax.set_aspect('equal') and ax.axis('equal') not working for 3D.

    Input
      ax: a matplotlib axis, e.g., as output from plt.gca().
    '''

    x_limits = ax.get_xlim3d()
    y_limits = ax.get_ylim3d()
    z_limits = ax.get_zlim3d()

    x_range = abs(x_limits[1] - x_limits[0])
    x_middle = np.mean(x_limits)
    y_range = abs(y_limits[1] - y_limits[0])
    y_middle = np.mean(y_limits)
    z_range = abs(z_limits[1] - z_limits[0])
    z_middle = np.mean(z_limits)

    # The plot bounding box is a sphere in the sense of the infinity
    # norm, hence I call half the max range the plot radius.
    plot_radius = 0.5*max([x_range, y_range, z_range])

    ax.set_xlim3d([x_middle - plot_radius, x_middle + plot_radius])
    ax.set_ylim3d([y_middle - plot_radius, y_middle + plot_radius])
    ax.set_zlim3d([z_middle - plot_radius, z_middle + plot_radius])



R = 3.
s_multiplier = 1.
def get_shape(t, s):
    inner = R + s_multiplier * s * math.cos(0.5 * t)
    x = math.cos(t) * inner
    y = math.sin(t) * inner
    z = s * math.sin(0.5 * t)
    return (x, y, z)

X = []
Y = []
Z = []


for t in np.linspace(0, 4 * math.pi):
    (x, y, z) = get_shape(t, 1.)
    X.append(x)
    Y.append(y)
    Z.append(z)


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot(X, Y, Z, "r")

X = []
Y = []
Z = []

for t in np.linspace(0, 2 * math.pi, 61):
    for s in np.linspace(-0.9, 0.9, 5):
        (x, y, z) = get_shape(t, s)
        X.append(x)
        Y.append(y)
        Z.append(z)
ax.scatter(X, Y, Z)

set_axes_equal(ax)

plt.show()

