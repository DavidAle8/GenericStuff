import numpy as np
import scipy as sci
from copy import deepcopy
import numpy as np
import matplotlib.pyplot as plt
from projeto.morfologia import *
from helpers import plot_matriz, leitor_pbm

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
print(f"Máscara_2: \n{mascara_2} \n")
print(f"Imagem_2: \n{imagem_2} \n")
print(f"Imagem_2 erodida pela mascara_2: \n{imagem_erodida}  \n")
print("\n")
#plot_matriz(imagem_erodida) #Testar em um Colab ou jupyter notebook.


imagem_dilatada = dilatar(imagem_2, mascara_2)
print(f"Imagem_2 dilatada pela mascara_2: \n{imagem_dilatada} \n")
print("\n")
#plot_matriz(imagem_dilatada) #Testar em um Colab ou jupyter notebook.


imagem_abertura= abertura(imagem_2, mascara_2)
print(f"Resultado da abertura da imagem_2: \n{imagem_abertura} \n")
print("\n")
#plot_matriz(imagem_abertura) #Testar em um Colab ou jupyter notebook.


imagem_fechamento = fechamento(imagem_2, mascara_2)
print(f"Resultado da abertura da imagem_2: \n{imagem_fechamento} \n")
print("\n")
#plot_matriz(imagem_fechamento) #Testar em um Colab ou jupyter notebook.


img_fechamento_buraco = fechamento(img_buraco.copy(), mascara_1)
complemento_img_buraco = complemento(img_buraco.copy())
img_fechamento_buraco_cp = complemento(img_fechamento_buraco)

print(f"Máscara_1: \n{mascara_1} \n")
print(f"Imagem_buraco: \n{img_buraco} \n")
print(f"Fechamento Imagem_buraco: \n{img_fechamento_buraco} \n")
print(f"Complemento Imagem_buraco: \n{complemento_img_buraco} \n")
print(f"Resultado complemento da img_buraco fechada: \n{img_fechamento_buraco} \n")
print("\n")
#plot_matriz(img_fechamento_buraco) #Testar em um Colab ou jupyter notebook.
#plot_matriz(img_fechamento_buraco_cp) #Testar em um Colab ou jupyter notebook.


