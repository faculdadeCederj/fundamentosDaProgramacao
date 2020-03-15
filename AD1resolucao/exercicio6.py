'''
6 a Questão (2,0 pontos)
Faça um programa que peça ao usuário as dimensões de uma matriz bidimensional, chamada
de valores, de números inteiros a ser gerada em aleatoriamente no intervalo 10 a 99. Via
subprogramação:
•
•
•
Mostre a matriz gerada;
Ordene as linhas da matriz em ordem crescente da soma de seus valores;
Mostre a matriz ordenada.
Nesse programa, seu programa DEVE implementar e utilizar o método da partição.
'''

# SUBPROGRAMAS

def trataEntrada(dimensao):
    tamanho = len(dimensao)
    if tamanho == 2:
        for indice in range(tamanho):
            dimensao[indice] = int(dimensao[indice])
    else:
        print('dimensao invalida!!')

def constroiMatriz(dimensao):
    from random import randint
    global matriz
    matriz = list()

    for linha in range(dimensao[0]):
        matriz.append(list())
        for coluna in range(dimensao[1]):
            matriz[linha].append(randint(10, 99))
    return matriz


def imprimeMatriz(matriz):
    qtd_linhas = len(matriz)
    qtd_colunas = len(matriz[0])
    for linha in range(qtd_linhas):
        for coluna in range(qtd_colunas):
            if coluna == 0:
                print('\n', end='')
            print(matriz[linha][coluna], end='\t')


def ordenaLinhas(matriz):
    soma = list()
    qtd_linhas = len(matriz)
    qtd_colunas = len(matriz[0])
    for linha in range(qtd_linhas):
        soma.append(0)
        for coluna in range(qtd_colunas):
            soma[linha] += matriz[linha][coluna]

    for linha in range(qtd_linhas):
        if linha == 0:
            continue
        else:
            if soma[linha] < soma[linha -1]:
                aux = matriz[linha - 1]
                matriz[linha - 1] = matriz[linha]
                matriz[linha] = aux
                aux = soma[linha - 1]
                soma[linha - 1] = soma[linha]
                soma[linha] = aux


# VARIAVEIS
entrada = list()

# PROGRAMA PRINCIPAL
entrada.append(input())
entrada.append(input())
trataEntrada(entrada)
constroiMatriz(entrada)
imprimeMatriz(matriz)
ordenaLinhas(matriz)
print('')
imprimeMatriz(matriz)