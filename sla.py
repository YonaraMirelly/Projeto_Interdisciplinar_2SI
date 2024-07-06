# Import "permutations"
from itertools import permutations
from sys import maxsize

# Dicionário para armazenar os pontos e suas coordenadas
pontos = {}

# Abertura do txt e mapeamento da matriz
with open('rota.txt', 'r') as matriz_entrada:
    matriz = []
    for i in matriz_entrada:
        matriz.append(i.split())
    matriz.remove(matriz[0]) # Remoção da linha informativa sobre a Qtd de linhas e colunas

    # Localizando os pontos e suas coordenadas na matriz
    for l in range(len(matriz)): # Número de linhas dentro da matriz
        for c in range(len(matriz[0])): # Número de elementos dentro das linhas
            if matriz[l][c] != '0':
                pontos[matriz[l][c]] = [l, c]

print(pontos)

# Função de calculo de distância entre os pontos
def distancias(Coord1, Coord2):
    return abs( (Coord1[0]) - (Coord2[0]) ) + abs( (Coord1[1]) - (Coord2[1]) )

# Permutando as rotas
recebidos = permutations(pontos)

# Calculando a distância das rotas e encontrando a menor delas
distancia = []
rotas = {maxsize: ('R','D')}
for i in list(recebidos):
    if i[0] == 'R':
        for coordenada in range(len(i) - 1):
            distancia.append(distancias(pontos[i[coordenada]], pontos[i[coordenada + 1]]))

        # Realizando o cálculo da volta ao ponto inicial (R)
        distancia.append(distancias(pontos[i[coordenada + 1]], pontos['R'] ))

        # Transformando a key de rotas em um inteiro para seleção da menor rota
        menor_rota_anterior = list(rotas.keys())
        if sum(distancia) < int(menor_rota_anterior[0]):
            rotas.clear()
            rotas[sum(distancia)] = i
        distancia = []

        # Verificando a evolução da menor rota
        # print(rotas)

# Menor rota
print(rotas)

# Removendo o ponto 'R' da menor rota e a transformando em uma string
menor_rota = list(rotas[int(menor_rota_anterior[0])])
if 'R' in menor_rota:
    menor_rota.remove('R')
print(' '.join(menor_rota))