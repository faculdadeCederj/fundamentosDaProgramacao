#SUBPROGRAMAS
def palindromo(palavra):
  tamanho = len(palavra)

  if tamanho > 1:
    if palavra[0] != palavra[-1]:
      return False
    else:
      palavra = palavra[1:-2]
      palindromo(palavra)
      
  return True


#PROGRAMA PRINCIPAL
saida = list()
entrada = input()

try:
  with open(entrada, 'r') as arquivo:
    for linha in arquivo:
      linhalst = linha.split()
      for palavrap in linhalst:
        nalista = False
        if palindromo(palavrap):
          for paliTrue in saida:
            if palavrap == paliTrue:
              nalista = True
              break
          if nalista == False:
            saida.append(palavrap)

  for palavra in saida:
    print(palavra)

except OSError:
  print('Erro na leitura do arquivo.')


