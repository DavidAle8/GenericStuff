import numpy as np
from copy import deepcopy
from collections import deque
from projeto.solucao_dfs import *
from Helpers.leitor_pbm import ler_pbm


""" Este arquivo executa as funções da pasta projeto, necessariamente a solucao_dfs.py que foi
    a técnica chave utilizada para solução do problema.
    
    OBS:AS IMAGENS PASSADAS PARA O ALGORITMO PRECISAM SER UMA CÓPIA DA IMAGEM ORIGINAL PARA FUNCIONAMENTO!!!
    SEMPRE PASSAR *imagem_que_deseja*.copy()
"""

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

# Teste com a matriz img_buraco.

# Copia da imagem original passada 
vetor_de_objetos = colecao_de_objetos(img_buraco.copy())
resultado = detectar_buracos(vetor_de_objetos)

#print(resultado)


# Teste com uma imagem.pbm.
caminho_imagem = "imagens/imagem1.pbm"

img_pmb = ler_pbm(caminho_imagem)
objetos = colecao_de_objetos(img_pmb.copy())
resultado_final = detectar_buracos(objetos)

print(resultado_final)