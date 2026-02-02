import numpy as np


""" Ler um arquivo PBM e constrói uma matriz do zero para cada pixel lido do conteúdo do pbm. """
def ler_pbm(caminho):
    
    with open(caminho, "r") as f:
        linhas = f.readlines()

    linhas = [l.strip() for l in linhas if l.strip()]

    dimensao = linhas[2]
    largura, altura = map(int, dimensao.split())

    dados = linhas[3:]

    pixels = []
    for linha in dados:
        for c in linha:
            if c == '0' or c == '1':
                pixels.append(int(c))

    matriz = np.array(pixels, dtype=np.uint8).reshape(altura, largura)

    return matriz
