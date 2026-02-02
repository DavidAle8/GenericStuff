from copy import deepcopy
import numpy as np



""" Cria uma matriz limpa/descolorida (só com 0's/fundo) do tamanho da imagem. """
def matriz_base(x, y):
    matriz = np.zeros((x, y), dtype=int)
    return matriz




""" Busca a posição (x,y) da origem da máscara e retorna. """
def origem_mascara(mascara):
    matriz = np.array(mascara)
    resultado = np.argwhere(matriz == 8)
    x, y = resultado[0]
    return x, y



""" Busca as posições (x,y) dos pixels 1 da máscara e retorna um vetor com essas posições. """
def posicoes_1_mascara(mascara):
    posicoes = []
    for i in range(len(mascara)):
        for j in range(len(mascara[0])):
            if mascara[i][j] == 1 or mascara[i][j] == 8:
                posicoes.append((i,j))

    return posicoes



""" Calcula o deslocamento de cada um dos pixels 1 da máscara baseado na origem. """
""" Diz quanto que eu devo andar para chegar a esses pixels 1 da máscara. """
def deslocamento(mascara):

    x, y = origem_mascara(mascara)
    posicoes = posicoes_1_mascara(mascara)
    deslocamentos = []
    for k, l in posicoes:
        dk = k - x
        dl = l - y
        deslocamentos.append((dk, dl))

    return deslocamentos



""" Retorna a imagem dilatada. Quando um pixel 1 da img é encontrado, uso os deslocamentos dos pixels 1
da máscara para saber onde pintar alí naquele momento da imagem baseado na origem atual (pixel 1 da img).
"""
def dilatar(imagem, mascara):

    m = len(imagem)
    n = len(imagem[0])

    imagem_dilatada = matriz_base(m, n)
    deslocamentos = deslocamento(mascara)

    for i in range(m):
        for j in range(n):
            if imagem[i][j] == 1:
                for dk, dl in deslocamentos:
                    if 0 <= i+dk < m and 0 <= j+dl < n:
                        imagem_dilatada[i+dk][j+dl] = 1

    return imagem_dilatada



""" Retorna a imagem erodida. Pega cada ponto da imagem na qual estaria tbm os pixels 1 da máscara
para saber se nesses pontos os pixels dela (da imagem) é 1, para saber se a máscara coube alí.
"""
def erodir(imagem, mascara):

    m = len(imagem)
    n = len(imagem[0])

    imagem_erodida = matriz_base(m, n)
    deslocamentos = deslocamento(mascara)

    for i in range(m):
        for j in range(n):
            pode_pintar = True
            for dk, dl in deslocamentos:
                if not (0 <= i+dk < m and 0 <= j+dl < n):
                    pode_pintar = False
                    break
                if imagem[i+dk][j+dl] == 0:
                    pode_pintar = False
                    break
            if pode_pintar:
                imagem_erodida[i][j] = 1

    return imagem_erodida



""" Erodi depois dilata """
def abertura(imagem, mascara):
    imagem_erodida = erodir(imagem, mascara)
    imagem_final = dilatar(imagem_erodida, mascara)
    return imagem_final



""" dilata depois erodi """
def fechamento(imagem, mascara):
    imagem_dilatada = dilatar(imagem, mascara)
    imagem_final = erodir(imagem_dilatada, mascara)
    return imagem_final



""" Retorna o complemento da imagem (inverte os pixels da imagem de entrada)"""
def complemento(imagem):

    imagem_copia = deepcopy(imagem)

    for i in range(len(imagem_copia)):
        for j in range(len(imagem_copia[0])):
            if imagem_copia[i][j] == 1:
                imagem_copia[i][j] = 0
            else:
                imagem_copia[i][j] = 1

    return imagem_copia




""" Subtrai uma imagem com a outra. Para isso é necessário fazer uma interseção entre a imagem A com o complemento da B.
    A ∩ Bᶜ
"""
def subtracao(imagem_A, imagem_B):

    imagem_final = deepcopy(imagem_A)
    c_imagem_B = complemento(deepcopy(imagem_B))

    for i in range(len(imagem_A)):
        for j in range(len(imagem_A[0])):
            if imagem_A[i][j] == 1 and c_imagem_B[i][j] == 1:
                imagem_final[i][j] = 1
            else:
                imagem_final[i][j] = 0
    return imagem_final
