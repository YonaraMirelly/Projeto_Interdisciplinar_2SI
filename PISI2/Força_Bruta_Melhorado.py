"""
------------------------------------------------------
PROJETO INTERDISCIPLINAR PARA SISTEMAS DE INFORMAÇÃO 2 
Nome: Yonara Mirely Araújo da Silva
Projeto: FlyFood
------------------------------------------------------
"""

from itertools import permutations
from sys import maxsize
import time

inicial = time.time()

# Armazenar os pontos da matriz e as suas respectivas coordenadas
pontos = {}

# Abrir o arquivo .txt
with open("PISI2/rota.txt", "r") as entrada:
    matriz = []
    # Para cada linha no arquivo
    for i in entrada:
        matriz.append(i.split())  # Dividir cada elemento i de entrada pelo método split(), tendo por base os espaços e adicionar à lista 'matriz'.
    matriz.remove(matriz[0])  # Remover a primeira linha do arquivo pois não utilizarei

    # Localizar os pontos e as coordenadas
    for l in range(len(matriz)):  # Iterar sobre cada linha da matriz
        for c in range(len(matriz[0])):  # Número de elementos dentro da linha
            if matriz[l][c] != "0":  # Verifica se o elemento é 0 ou não
                pontos[matriz[l][c]] = [l, c]  # Adiciona no Dicionário a chave como ponto e o seu respectivo valor como coordenada

# Calcular as distâncias entre os pontos
def distancias(ponto1, ponto2):  # Recebe as coordenadas dos pontos
    return abs(ponto1[0] - ponto2[0]) + abs(ponto1[1] - ponto2[1])

# Separar o ponto "R" dos demais pontos
ponto_inicial = "R"
outros_pontos = [p for p in pontos.keys() if p != ponto_inicial]

# Permutando as rotas utilizando a biblioteca
permutações = permutations(outros_pontos)

# Calcular todas as distâncias e encontrar a menor delas
rotas = {maxsize: ("R", "D")}

# Cada permutação é uma rota potencial. O laço itera sobre todas as permutações possíveis dos pontos
for i in list(permutações):
    rota = [ponto_inicial] + list(i) + [ponto_inicial]  # Garantir que todas as rotas comecem e terminem em "R"
    acumulador_distancia = 0  # Inicializar o acumulador de distâncias
    for coordenada in range(len(rota) - 1):
        acumulador_distancia += distancias(pontos[rota[coordenada]], pontos[rota[coordenada + 1]])

    # Seleção da menor rota
    menor_rota = list(rotas.keys())
    if acumulador_distancia < int(menor_rota[0]):
        rotas.clear()
        rotas[acumulador_distancia] = rota

# Tirar o 'R' e formatar em uma única string visual
menor_rota_visual = list(rotas[min(rotas.keys())])
menor_rota_visual.remove("R")
if menor_rota_visual[-1] == ponto_inicial:
    menor_rota_visual.pop()

# Printar na tela a menor rota e a menor distância
print('=== FlyFood ===')
print('A menor rota é:')
print(" -> ".join(menor_rota_visual))
print(f'A menor distância é: {min(rotas.keys())}')

# Verificar o tempo de Execução do Algoritmo
final = time.time()
print("Tempo de execução: ", final - inicial)
