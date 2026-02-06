import numpy as np
from copy import deepcopy
from projeto.morfologia import *   
from collections import deque


""" Retorna as posições dos pixels da vizinhança 8 do pixel atual """
def vizinhanca_8(x,y):

    posições_vizinho_8 = [
      (x-1, y-1), (x-1, y), (x-1, y+1),
      (x,   y-1),           (x,   y+1),
      (x+1, y-1), (x+1, y), (x+1, y+1)
    ]

    return posições_vizinho_8



""" Retorna as posições dos pixels da vizinhança 4 do pixel atual """
def vizinhanca_4(x,y):

    posições_vizinho_4 = [
                (x,y+1),
        (x-1,y)        ,(x+1,y)
               ,(x,y-1)
    ]

    return posições_vizinho_4




""" Algoritmo de busca em profundidade para detectar objetos com a vizinhança 8. 
    O mesmo retorna as posições onde se encontraram os pixels 1's do objeto, marcando-os.
"""
def dfs_8(imagem, x, y):

    fronteira = [(x,y)]
    imagem[x][y] = 2
    posicoes_objeto = [(x,y)]

    while fronteira:
        cx, cy = fronteira.pop()
        for nx, ny in vizinhanca_8(cx, cy):
            if (0 <= nx < len(imagem) and 0 <= ny < len(imagem[0])) and imagem[nx][ny] == 1:
                imagem[nx][ny] = 2
                fronteira.append((nx, ny))
                posicoes_objeto.append((nx, ny))

    return posicoes_objeto



"""
    Cria uma matriz para aquele objeto encontrado na imagem e retorna-o.
    Após receber como parâmetro as posições dos pixels 1 da imagem que foram marcadas,
    descubro os i's e j's maximos e mínimos das posições e subtraio para obter os tamanhos e além disso
    subtraio cada posição dos pixels marcados por um referencial também dos pixels marcados (foi usado o minimo i e j 
    de tdoas as posições dos pixels marcados como ref.) para saber onde eles se encontrariam/seriam 
    pintados na matriz limpa matriz_resultante.
"""
def criar_matriz_objeto(pos_objeto):

    max_i = max(p[0] for p in pos_objeto)
    min_i = min(p[0] for p in pos_objeto)
    max_j = max(p[1] for p in pos_objeto)
    min_j = min(p[1] for p in pos_objeto)

    m = max_i - min_i + 1
    n = max_j - min_j + 1

    # A posição de referência é a posição do pixel marcado com menor i e j (ele equivale ao (0,0) da matriz limpa)
    ref_i = min_i
    ref_j = min_j
    
    matriz_resultante = matriz_base(m, n)

    for i, j in pos_objeto:
        cord_i = i - ref_i
        cord_j = j - ref_j
        matriz_resultante[cord_i][cord_j] = 1

    return matriz_resultante



""" Cria e retorna um vetor contendo todos os objetos da imagem após serem detectadas pelo dfs_8 e 
    terem sua matriz criada no criar_matriz_objeto.
"""
def colecao_de_objetos(imagem):

    colecao_objetos = []
    
    for i in range(len(imagem)):
        for j in range(len(imagem[0])):
            if imagem[i][j] == 1:
                posicoes_objeto = dfs_8(imagem, i, j)
                matriz_objeto = criar_matriz_objeto(posicoes_objeto)
                colecao_objetos.append(matriz_objeto)

    return colecao_objetos



""" No pseudo_dfs_4 buscamos buracos (pixels 0) verificando se ele está nas bordas do objeto.
    Caso esteja, caso algum pixel 0 de um candidato a ser buraco toque a borda, então a condição de 
    ser buraco falha colocamos que ele toca a borda (toca_borda = True), se não, retornamos que ele
    não toca, e por isso se torna buraco (not toca_borda)
"""
def pseudo_dfs_4(objeto, x, y):

    fronteira = [(x,y)]
    visitados = [(x,y)]
    toca_borda = False

    while fronteira:
        cx, cy = fronteira.pop()
        if cx == 0 or cy == 0 or cx == len(objeto)-1 or cy == len(objeto[0])-1:
            toca_borda = True
            break
        for nx, ny in vizinhanca_4(cx, cy):
            if (0 <= nx < len(objeto) and 0 <= ny < len(objeto[0])) and objeto[nx][ny] == 0 and (nx, ny) not in visitados:
                fronteira.append((nx, ny))
                visitados.append((nx, ny))

    return not toca_borda



""" Percorre minha matriz de objetos, analisa cada um e aplica o pseudo_dfs_4 para achar buracos em cada um deles
    e retorna a quantidade de todos os objetos, dos esburacados e os não esburacados.
"""
def detectar_buracos(colecao_objetos):

    objetos_esburacados = 0
    objetos_nao_esburacados = 0

    for objeto in colecao_objetos:
        buraco = False
        for i in range(len(objeto)):
            for j in range(len(objeto[0])):
                if objeto[i][j] == 0:
                    if pseudo_dfs_4(objeto, i, j):
                        buraco = True
                        break

        if buraco:
            objetos_esburacados += 1
        else:
            objetos_nao_esburacados += 1

    return f"\nTotal de objetos: {objetos_esburacados + objetos_nao_esburacados} \nObjetos com buracos: {objetos_esburacados} \nObjetos sem buracos: {objetos_nao_esburacados}\n"
