'''
5 a Questão (1,5 pontos)
Considere a existência de uma linha vertical que representa o intervalo [0, 2 n ]. Agora desenhe
traços verticais apoiados nos pontos 1, 2, 3, ... 2 n -1 da linha vertical imaginária. O traço vertical
no ponto médio do intervalo deve ter altura n, os traços nos pontos médios dos subintervalos
esquerdo e direito têm altura n-1, e assim por diante. Diremos que isso é uma régua de ordem n
no intervalo [0, 2 n ].
Dado o valor de n, escreva um programa recursivo que escreva tal régua na saída padrão.
Entrada
A entrada é composta por um único valor n inteiro não negativo.
Saída
A régua impressa da saída padrão com o formato conforme apresentado no exemplo.
'''

# SUBPROGRAMAS

def imprimetracos(qtd):
    return (qtd * '-')

def calculatracos(entrada):
     tamanho = 2 ** entrada
     postraco[1] = 1
     for medida in range(2, tamanho):
         if medida % 2 == 0:
            postraco[medida] = postraco[medida//2] + 1
         else:
             postraco[medida] = 1



def imprimeregua(entrada):
    tamanho = 2 ** entrada
    for medida in range(1, tamanho):
        if medida < 10:
            print(f'0{medida} {imprimetracos(postraco[medida])}')
        else:
            print(f'{medida} {imprimetracos(postraco[medida])}')


# VARIAVEIS
postraco = dict()

# PROGRAMA PRINCIPAL
entrada = int(input('Insira um valor inteiro nao negativo: '))
calculatracos(entrada)
imprimeregua(entrada)