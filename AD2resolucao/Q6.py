#SUBPROGRAMAS
def mdc(a, b):
  if b > 0:
    return mdc(b, a % b)
  else:
    return a


#PROGRAMA PRINCIPAL
try:
  with open('valores.bin', 'rb') as arq:
    n = arq.read(4)
    for val in range(int(n)):
      a = arq.read(4)
      b = arq.read(4)
      print(mdc(int(a),int(b)))

except OSError:
  print('Erro na leitura do arquivo')
  
