#SUBPROGRAMAS
def insereOrdenado(nomeDoArquivo, novoValor):
  try:
    with open(nomeDoArquivo, 'rb+') as arq:
      arq.seek(0,2)
      tam = arq.tell()
      arq.seek(0,0)
      for item in arq:
        if float(item) >= novoValor:
          arq.seek(-len(item), 1)
          pos = arq.tell()
          apos = arq.readlines()
          apos.insert(0, bytes(str(novoValor)+'\n', 'utf-8'))
          arq.seek(pos,0)
          for item in apos:
            arq.write(item)
          break
        elif arq.tell() == tam:
          arq.write(bytes('\n'+str(novoValor), 'utf-8'))
          
  except OSError:
    print('Falha na leitura')

#PROGRAMA PRINCIPAL
insereOrdenado("teste.txt", 6.0)

'''
entradas
4.6
5.12
5.12
6.8
8.5
8.67
'''