'''
2 a Questão (1,5 pontos)
Utilizando subprogramação, faça um programa que leia da entrada padrão uma linha podendo
conter vários números de ponto flutuante. Caso exista, escreva qual o número que mais ocorreu
e a quantidade de vezes que ocorreu. Caso haja empate escreva um deles. Caso a linha lida
seja uma string vazia, escreva a mensagem: “nenhum número foi lido!!!”
'''

# SUBPROGRAMAS


def lerString(lista_float):
    lista_float[:] = input('Escreva uma string contendo numeros de ponto flutuante separados por " ": ').split()
    return lista_float

def maiorFrequencia(lista_float):
    contagem_valor = 0
    valor_maior_freq = 0
    tamanho = len(lista_float)

    if tamanho == 0:
        print('nenhum numero foi lido!!!')
    else:
        for num, valor in enumerate(lista_float):
            qtd = lista_float.count(valor)
            if qtd > contagem_valor:
                contagem_valor = qtd
                valor_maior_freq = valor
        print(f'O numero que mais ocorreu foi o {valor_maior_freq}.')
        print(f'Ele ocorreu {contagem_valor} vezes.')


# VARIAVEIS
entrada = list()

# PROGRAMA PRINCIPAL
lerString(entrada)
maiorFrequencia(entrada)
