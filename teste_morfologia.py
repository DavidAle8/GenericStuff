import numpy as np
import scipy as sci
from copy import deepcopy
import numpy as np
import matplotlib.pyplot as plt
from projeto.morfologia import *
from Helpers import plot_matriz, leitor_pbm

""" 
    Este arquivo foi criado para testar e visualziar o funcionamento das funções que envolve as técnicas de morfologia.
    Caso queira utilizar uma das imagens pbm, lembrar de utilizar leitor_pbm para gerar uma matriz da imagem e utilizá-la.
    
"""


mascara_v4 = np.array([
    [0, 1, 0],
    [1, 8, 1],
    [0, 1, 0]
])

mascara_v8 = np.array([
    [1, 1, 1],
    [1, 8, 1],
    [1, 1, 1]
])

mascara_1 = np.array([
    [0, 1, 0],
    [0, 8, 1],
    [0, 0, 0]
])

mascara_2 = np.array([
    [0, 0, 0],
    [0, 8, 1],
    [0, 0, 0]
])

imagem_1 = np.array([
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0]
])

imagem_2 = np.array([
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 1, 1, 0, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
])


img_buraco = np.array([
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,1,1,1,1,0,0,0,0,1,1,1,1,0],
    [0,0,1,0,1,1,0,0,0,0,1,0,0,1,0],
    [0,0,1,1,1,1,0,0,0,0,1,1,1,1,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
])



imagem_erodida = erodir(imagem_2, mascara_2)
print(f"{mascara_2} \n")
print(f"{imagem_2} \n")
print(f"{imagem_erodida}  \n")
#plot_matriz(imagem_erodida) #Testar em um Colab ou jupyter notebook.



imagem_dilatada = dilatar(imagem_2, mascara_2)
print(f"{mascara_2} \n")
print(f"{imagem_2} \n")
print(f"{imagem_dilatada} \n")
#plot_matriz(imagem_dilatada) #Testar em um Colab ou jupyter notebook.



imagem_abertura= abertura(imagem_2, mascara_2)
print(f"{mascara_2} \n")
print(f"{imagem_2} \n")
print(f"{imagem_abertura} \n")
#plot_matriz(imagem_abertura) #Testar em um Colab ou jupyter notebook.



imagem_fechamento = fechamento(imagem_2, mascara_2)
print(f"{mascara_2} \n")
print(f"{imagem_2} \n")
print(f"{imagem_fechamento} \n")
#plot_matriz(imagem_fechamento) #Testar em um Colab ou jupyter notebook.



img_fechamento_buraco = fechamento(img_buraco, mascara_1)
img_fechamento_buraco_cp = complemento(img_fechamento_buraco)
print(f"{mascara_1} \n")
print(f"{img_buraco} \n")
print(f"{img_fechamento_buraco} \n")
#plot_matriz(img_fechamento_buraco) #Testar em um Colab ou jupyter notebook.
#plot_matriz(img_fechamento_buraco_cp) #Testar em um Colab ou jupyter notebook.