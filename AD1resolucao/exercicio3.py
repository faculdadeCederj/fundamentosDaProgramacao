'''
3 a Questão (2,0 pontos)
Utilizando subprogramação, faça um programa que leia da entrada padrão, em uma única
string, dois números inteiros separados por um espaço em branco, representando as duas
dimensões de uma matriz bidimensional. Construa uma matriz bidimensional com as dimensões
lidas e com valores gerados aleatoriamente, via função randint importada do módulo
random, no intervalo 100 a 999.
Escreva:
(1) O conteúdo da matriz, onde cada linha a ser escrita possua apenas números inteiros, sem
vírgulas nem colchetes;
(2) A posição (linha, coluna) do maior valor sorteado e o seu respectivo valor;
(3) A soma de cada linha, de todas as linhas da matriz;
(4) A soma de cada coluna, de todas as colunas da matriz.
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
            matriz[linha].append(randint(100, 999))
    return matriz


def imprimeMatriz(matriz):
    qtd_linhas = len(matriz)
    qtd_colunas = len(matriz[0])
    print('O conteudo da matriz possuindo apenas numeros inteiros e: ')
    for linha in range(qtd_linhas):
        for coluna in range(qtd_colunas):
            if coluna == 0:
                print('\n', end='')
            print(matriz[linha][coluna], end='\t')


def maiorValor(matriz):
    maior = 0
    col_maior = 0
    lin_maior = 0
    qtd_linhas = len(matriz)
    qtd_colunas = len(matriz[0])

    for linha in range(qtd_linhas):
        for coluna in range(qtd_colunas):
            if matriz[linha][coluna] > maior:
                maior = matriz[linha][coluna]
                col_maior = coluna
                lin_maior = linha
    print(f'\n\nO maior valor ({maior}) esta na linha {lin_maior + 1} e na coluna {col_maior + 1}.')



def somaLinhas(matriz):
    qtd_linhas = len(matriz)
    qtd_colunas = len(matriz[0])
    for linha in range(qtd_linhas):
        soma = 0
        for coluna in range(qtd_colunas):
            soma += matriz[linha][coluna]
        print(f'A soma dos elementos da linha {linha + 1} e {soma}.')

def somaColunas(matriz):
    qtd_linhas = len(matriz)
    qtd_colunas = len(matriz[0])
    for coluna in range(qtd_colunas):
        soma = 0
        for linha in range(qtd_linhas):
            soma += matriz[linha][coluna]
        print(f'A soma dos elementos da coluna {coluna + 1} e {soma}.')


# PROGRAMA PRINCIPAL
entrada = input('Digite uma string contendo 2 inteiros separados por um espaco em branco: ').split()
trataEntrada(entrada)
constroiMatriz(entrada)
imprimeMatriz(matriz)
maiorValor(matriz)
somaLinhas(matriz)
somaColunas(matriz)