import numpy as np
import scipy as sci
import numpy as np
import matplotlib.pyplot as plt



""" Plota a matriz para melhor visualização delas. """
def plot_matriz(matriz):
    
    h, w = matriz.shape

    plt.figure(figsize=(6, 6))
    plt.imshow(matriz, cmap='gray_r', interpolation='nearest')
    plt.xticks(np.arange(-0.5, w, 1))
    plt.yticks(np.arange(-0.5, h, 1))

    plt.grid(color='green', linestyle='-', linewidth=1)

    plt.tick_params(left=False, bottom=False, labelleft=False, labelbottom=False)

    plt.show()
    print("\n")
