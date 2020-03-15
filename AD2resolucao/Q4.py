q = 0
e = 0
dia = list()
sem = list()

try:
  with open('entradas.bin', 'rb') as entrada:
      q = entrada.read(4)
      e = entrada.read(4)
      for s in range(int(e)):
        dia.append(entrada.read(4))
      for c in range(int(q)):
        sem.append(entrada.read(4))

except OSError:
  print('Erro na leitura do arquivo de entrada')

# O NUMERO 88 SE REPETE, MAS NÃO APARECE NA SAIDA
# PORQUE ESTOU USANDO SET, QUE DISCARTA REPETIDOS
# CASO NECESSÁRIO, USAR DICIONARIOS, COM CHAVES
# NUMERICAS
with open('saida.bin', 'wb') as saida:
  for cliente in sem:
    if cliente in dia:
      saida.write(b'0000')
    else:
      saida.write(b'0001')
