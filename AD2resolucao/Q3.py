#SUBPROGRAMAS
def menordist(pontos, centroide):
  menorind = 0

  for index, ponto in enumerate(pontos):
    dist = ((ponto[0]-centroide[0])**2 + (ponto[1]-centroide[1])**2)**(1/2)
    if index == 0:
      menordist = dist
    else:
      if dist < menordist:
        menorind = index
        menordist = dist
  stringmenor = f'{pontos[menorind][0]}, {pontos[menorind][1]}'
  return stringmenor
    


# PROGRAMA PRINCIPAL
somax = 0.0
somay = 0.0
qtdpontos = 0
arqentrada = input()
listapontos = list()

try:
  with open(arqentrada, 'r') as entradas:
    for ponto in entradas:
      pontocoord = ponto.split()
      pontocoord[0] = float(pontocoord[0])
      pontocoord[1] = float(pontocoord[1])
      listapontos.append(pontocoord)
      somax += pontocoord[0]
      somay += pontocoord[1]
      qtdpontos += 1 

except OSError:
  print('Erro na leitura do arquivo de entrada')
if qtdpontos != 0:
  centroidex = somax/qtdpontos
  centroidey = somay/qtdpontos
  centroide = [centroidex, centroidey]
  print(f'Centroide: ({centroidex:.1f}, {centroidey:.1f})')
  print(f'Ponto Mais Próximo: ({menordist(listapontos, centroide)})')