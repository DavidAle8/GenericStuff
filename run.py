import numpy as np
from collections import deque
from projeto.solucao_dfs import *
from helpers.leitor_pbm import ler_pbm


""" Este arquivo executa as funções da pasta projeto, necessariamente a solucao_dfs.py que foi
    a técnica chave utilizada para solução do problema.
    
    OBS:AS IMAGENS PASSADAS PARA O ALGORITMO PRECISAM SER UMA CÓPIA DA IMAGEM ORIGINAL PARA FUNCIONAMENTO!!!
    SEMPRE PASSAR *imagem_que_deseja*.copy()
"""



""" Matrizes básicas de exemplo: """
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


    
""" Teste com uma imagem.pbm. """

""" A maioria dos arquivos das imagens se chamam "imagem" com uma numeração, basta substituir o número para testar uma nova imagem.
    Com exceção das imagens sem_objetos e sem_buracos que são testes de imagens sem objetos e com objetos sem buracos envolvidos.
"""

caminho_imagem = "imagens/imagem1.pbm"

img_pmb = ler_pbm(caminho_imagem)
objetos = colecao_de_objetos(img_pmb.copy())
resultado_final = detectar_buracos(objetos)

print(resultado_final)