#SUBPROGRAMAS
def primo(num):
  if num > 1:
    for div in range(2, num):
      if num % div == 0:
        return False
    return True
  return False

#PROGRAMA PRINCIPAL
arqentradas = input()
arqsaidas = input()

try:
  with open(arqentradas, 'r') as entradas:
    for linha in entradas:
      linhaent = linha.split()
      linhaprimos = list()
      for num in linhaent:
        if primo(int(num)):
          linhaprimos.append(num)
      with open(arqsaidas, 'a') as saidas:
        linhaprimos = ' '.join(linhaprimos)
        saidas.write(f'{linhaprimos}\n')
    

except OSError:
  print('Falha na leitura do arquivo de entrada.')
