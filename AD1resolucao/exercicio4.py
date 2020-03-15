'''
4 a Questão (1,5 pontos)
A conversão de números inteiros para diferentes bases é uma operação realizada
frequentemente em computação. Por exemplo, no dia a dia estamos habituados a trabalhar
com números na base decimal. Entretanto, o computador opera na base binária. Enquanto,
eventualmente, a inspeção visual do conteúdo da memória do computador é feita na base octal
ou hexadecimal.
Faça um programa que, dados valores inteiros na binária, escreva na saída padrão cada valor
convertido para as bases 3 a 10.
Seu programa deve conter um subprograma que respeite o seguinte protótipo:
def converte(numBinario, base):
...
return numConvertido
'''

# SUBPROGRAMAS


def converte(numBinario, base):
    decimal = 0
    numConvertido = ''

    if numBinario == '0':
        numConvertido = '0'
        return numConvertido
    for pos in range(len(numBinario)):
        if numBinario[-(pos + 1)] == '1':
            decimal += 2 ** pos
    if base == 10:
        numConvertido = decimal
    else:
        while decimal > 0:
            numConvertido = str(decimal % base) + numConvertido
            decimal = decimal // base
    return numConvertido


def imprimesaida(entrada):
    for index, num in enumerate(entrada):
        print('')
        for base in range(3,11):
            print(converte(num, base), end=' ')


# VARIAVEIS
entrada = list()

# PROGRAMA PRINCIPAL
print('Digite o número a ser convertido, digite -1 para parar: ', end='')
entrada.append(input())
while entrada[-1] != '-1':
    entrada.append(input())
entrada.pop()
imprimesaida(entrada)




