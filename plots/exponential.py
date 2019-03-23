import numpy as np
import matplotlib.pyplot as plt

from src.expogen import Exp

def plot(name):
    color_sequence = ['#0000ff', '#00ff00', '#ff0000', '#000000']

    x_val = [x for x in np.arange(.001, 1, .001)]
    for mean in np.arange(.06, .6, .06):    
        e = Exp(mean)
        y_val = [e.inverse(x) for x in x_val] 


        plt.plot(x_val, y_val, color=color_sequence[int((mean * 100) // 6) % 4])

    plt.savefig(f'paper/images/{name}.png', bbox_inches='tight')
    plt.show()
