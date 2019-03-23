#!/usr/bin/python3
import numpy as np
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt

from analysis.means import sample

def plot(name='behaviour'):
    x_val = [x for x in np.arange(0, 1, .05) for _ in range(20)]
    y_val = [y for y in np.arange(60, 30 * 22, 30)] * 20
    z_val = [sample(y_val[i], x_val[i]) for i in range(len(x_val))]

    ax = plt.axes(projection='3d')
    ax.scatter3D(y_val, z_val, x_val)

    ax.set_xlabel('Valor Esperado')
    ax.set_ylabel('Mejora')
    ax.set_zlabel('sándwich / 100 clientes')

    plt.savefig(f'paper/images/{name}.png', bbox_inches='tight')
    plt.show()

if __name__ == "__main__":
    plot()

