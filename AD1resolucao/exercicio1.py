'''
1 a Questão (1,5 pontos)
Faça um programa que leia strings da entrada padrão até que a string vazia (“”) seja digitada.
Suponha que cada string não vazia seja convertível em um número de ponto flutuante.
Escreva:
(1) A quantidade de strings não vazias lidas;
(2) Caso exista: a média dos valores, das strings numéricas lidas;
(3) Caso exista: o valor do maior número lido.
'''

# SUBPROGRAMAS


def lerStrings(lista_str):
    while True:
        lista_str.append(str(input('Digite uma string, digite uma string vazia para sair: ')))
        if lista_str[-1] == '':
            lista_str.pop()
            break


def imprimeTamanho(lista_str):
    tamanho = len(lista_str)
    print(f'A quantidade de strings não vazias foi {tamanho}.')


def imprimeMedia(lista_str):
    media = 0.0
    tamanho = len(lista_str)
    if tamanho > 0:
        for num in range(tamanho):
            media += float(lista_str[num])
        media /= tamanho
        print(f'A media dos valores lidos foi {media:.3}.')
    else:
        print('Nao e possível calcular a media.')

def imprimeMaior(lista_str):
    maior = 0.0
    tamanho = len(lista_str)
    if tamanho > 0:
        for num in range(tamanho):
            if float(lista_str[num]) > maior:
                maior = float(lista_str[num])
        print(f'O maior número lido foi {maior}.')
    else:
        print('Nao e possível determinar o maior numero.')


# VARIAVEIS
entrada = list()

# PROGRAMA PRINCIPAL
lerStrings(entrada)
imprimeTamanho(entrada)
imprimeMedia(entrada)
imprimeMaior(entrada)

