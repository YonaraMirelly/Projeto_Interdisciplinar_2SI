from itertools import permutations
from sys import maxsize

# armazena os pontos da matriz e as suas respectivas coordenadas
pontos = {}

# abrir o arquivo
with open('rota.txt', 'r') as entrada:
    matriz = []
    for i in entrada:
        matriz.append(i.split())
    matriz.remove(matriz[0]) #remover a primeira linha do arquivo pois é apenas informativa

    # localizar os pontos e as coordenadas
    for l in range(len(matriz)): # n de linhas
        for c in range(len(matriz[0])): # n de elementos dentro da linha
            if matriz[l][c] != '0':
                pontos[matriz[l][c]] = [l, c] # chave = ponto ... valor = coordenada

#print(pontos)

# calcular as distâncias entre os pontos
def distancias(coordenada1, cooordenada2):
    return abs((coordenada1[0]) - (cooordenada2[0])) + abs( (coordenada1[1]) - (cooordenada2[1]))

# permutando as rotas
permutações = permutations(pontos)

# for j in recebidos:
#     print(j) # todas as combinações

# calcular todas as distâncias e encontrar a menor delas
distancia = []
rotas = {maxsize: ('R', 'D')}
for i in list(permutações):
    if i[0] == "R":
        for coordenada in range(len(i) - 1):
            distancia.append(distancias(pontos[i[coordenada]], pontos[i[coordenada+1]]))
        # voltando para o início = "R"
        distancia.append(distancias(pontos[i[coordenada+1]], pontos["R"]))

            # seleção da menor rota
        menor_rota = list(rotas.keys())
        if sum(distancia) < int(menor_rota[0]):
            rotas.clear()
            rotas[sum(distancia)] = i

        distancia = []

            #print(rotas)

# tirar o 'r' e formatar em uma única string visual
menor_rota_visual = list(rotas[int(menor_rota[0])])
if 'R' in menor_rota_visual:
    menor_rota_visual.remove('R')

print(' '.join(menor_rota_visual))