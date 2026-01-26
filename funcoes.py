import numpy as np
import scipy as sci

mascara_v4 = [
    [0,1,0],
    [1,8,1],   
    [0,1,0]
]

mascara_v8 = [
    [1,1,1],
    [1,8,1] ,  
    [1,1,1]
]

mascara_1 = [
    [0,1,0],
    [0,8,1],  
    [0,0,0]
]

mascara_2 = [
    [0, 0, 0],
    [0, 8, 1],
    [0, 0, 0]
]

imagem_1 = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0]
]



imagem_2 = [
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 1, 1, 0, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

def matriz_base(x, y):
    matriz = np.zeros((x, y), dtype=int)
    return matriz


def origem_mascara(mascara):
    matriz = np.array(mascara)
    resultado = np.argwhere(matriz == 8)
    linha, coluna = resultado[0]
    return linha, coluna


def posicoes_1_mascara(mascara):
    posicoes = []
    for i in range(len(mascara)):
        for j in range(len(mascara[0])):
            if mascara[i][j] == 1 or mascara[i][j] == 8:
                posicoes.append((i,j))
                
    return posicoes 


def deslocamento(mascara):
    
    x, y = origem_mascara(mascara)
    posicoes = posicoes_1_mascara(mascara)
    deslocamentos = []
    for k, l in posicoes:
        dk = k - x
        dl = l - y
        deslocamentos.append((dk, dl))

    return deslocamentos



def dilatar(imagem, mascara):
    
    x = len(imagem)
    y = len(imagem[0])
    
    imagem_dilatada = matriz_base(x, y)
    deslocamentos = deslocamento(mascara)
    
    for i in range(len(imagem)):
        for j in range(len(imagem[0])):
            if imagem[i][j] == 1:   
                for dk, dl in deslocamentos:
                    if 0 <= i+dk < len(imagem) and 0 <= j+dl < len(imagem[0]):
                        imagem_dilatada[i+dk][j+dl] = 1
    
    return imagem_dilatada



def erodir(imagem, mascara):
    
    x = len(imagem)
    y = len(imagem[0])

    imagem_erodida = matriz_base(x, y)
    deslocamentos = deslocamento(mascara)
    
    for i in range(len(imagem)):
        for j in range(len(imagem[0])): 
            pode_pintar = True
            for dk, dl in deslocamentos: 
                if not (0 <= i+dk < x and 0 <= j+dl < y):
                    pode_pintar = False
                    break
                if imagem[i+dk][j+dl] == 0:
                    pode_pintar = False
                    break
            if pode_pintar:
                imagem_erodida[i][j] = 1
                
    return imagem_erodida

       
#print(dilatar(imagem_1, mascara_1))
print(erodir(imagem_2, mascara_2))

""" 

Simulando a pintura no pixel (1,2) da imagem:

Pixel (0,1) cima:
dk = 0 - 1 = -1
dl = 1 - 1 =  0
→ deslocamento (-1, 0)


Pixel (1,1) → origem centro:
dk = 1 - 1 = 0
dl = 1 - 1 = 0
→ deslocamento (0, 0)


Pixel (1,2) direita:
dk = 1 - 1 = 0
dl = 2 - 1 = +1
→ deslocamento (0, +1)


Meus deslocamentos = [(-1, 0), (0, 0), (0, +1)]



Regra = (i + dk, j + dl)

Deslocamento (-1, 0) cima:
(i=1 + dk=-1, j=2 + dl=0) = (0,2) 

Deslocamento (0, 0) centro(origem):
(i=1 + dk=0, j=2 + dl=0) = (1,2)

Deslocamento (0, +1) direita:
(i=1 + dk=0, j=2 + dl=1) = (1,3)


resultado atual:
0 0 1 0 0 0 0
0 0 1 1 0 0 0
0 0 0 0 0 0 0




0 0 0 0 0 0 0
0 0 1 1 1 0 0
0 0 0 0 0 0 0

mascara: (0,1), (1,1), (2,1) e (2,2)
(0,0)=0,(0,1)=1,(0,2)=0
(1,0)=0,(1,1)=8,(2,2)=1 
(2,0)=0,(2,1)=0,(2,2)=0 

imagem:
(0,0)=0,(0,1)=0,(0,2)=0,(0,3)=0,(0,4)=0,(0,5)=0,(0,6)=0
(1,0)=0,(1,1)=0,(1,2)=1,(1,3)=1,(1,4)=1,(1,5)=0,(1,6)=0
(2,0)=0,(2,1)=0,(2,2)=0,(2,3)=0,(2,4)=0,(2,5)=0,(2,6)=0


imagem descolorida: 
(0,0)=0,(0,1)=0,(0,2)=1,(0,3)=1,(0,4)=0,(0,5)=0,(0,6)=0
(1,0)=0,(1,1)=0,(1,2)=1,(1,3)=1,(1,4)=1,(1,5)=0,(1,6)=0 
(2,0)=0,(2,1)=0,(2,2)=1,(2,3)=1,(2,4)=0,(2,5)=0,(2,6)=0



Mascara:
000
011
000


Imagem:
00000
00100
01100
01100
00100
00100
00000
00000

resultado:                                            
00000 
00000
01100
01100
00000
00000
00000
00000 




def erodir_2(imagem, mascara):
    
    x = len(imagem)
    y = len(imagem[0])
    posicoes_a_pintar = []
    
    imagem_erodida = matriz_base(x, y)
    deslocamentos = deslocamento(mascara)
    
    for i in range(len(imagem)):
        for j in range(len(imagem[0])): 
            for dk, dl in deslocamentos:
                if 0 <= i+dk < x and 0 <= j+dl < y:
                    if imagem[i+dk, j+dl] == 1:
                        posicoes_a_pintar.append((i+dk, j+dl))
                if 0 in posicoes_a_pintar:
                    for pos in posicoes_a_pintar:
                        imagem[pos[0]][pos[1]] = 1
                else:
                    break
                        


"""