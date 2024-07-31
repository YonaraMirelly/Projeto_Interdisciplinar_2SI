"""
------------------------------------------------------
PROJETO INTERDISCIPLINAR PARA SISTEMAS DE INFORMAÇÃO 2 
Nome: Yonara Mirely Araújo da Silva
Projeto: FlyFood
------------------------------------------------------
"""

from itertools import permutations # gerar todas as permutações possívei de uma lista
from sys import maxsize # serve para definir o valor inicial máximo
import time # serve para medir o tempo de execução

inicial = time.time() # tempo atual

# Armazenar os pontos da matriz e as suas respectivas coordenadas
pontos = {}

# Abrir o arquivo .txt
with open("PISI2/rota2.txt", "r") as entrada:
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
    # A distância de Manhattan é uma medida da distância entre dois pontos em uma grade baseada apenas em movimentos horizontais e verticais (não diagonais).
    # É a soma das diferenças absolutas de suas coordenadas, ou seja, X1-X2 + Y1-Y2.
    return abs(ponto1[0] - ponto2[0]) + abs(ponto1[1] - ponto2[1])

# Separar o ponto "R" dos demais pontos
ponto_inicial = "R"
outros_pontos = [p for p in pontos.keys() if p != ponto_inicial] # lista com todos os pontos exceto o "R" para agilizar o tempo durante as permutações

# Permutando as rotas utilizando a biblioteca
permutações = permutations(outros_pontos)

# Calcular todas as distâncias e encontrar a menor delas
rotas = {maxsize: ("R", "D")}

# Cada permutação é, de fato, uma rota potencial. Nesse sentido, o laço itera sobre todas as permutações possíveis dos pontos
for i in list(permutações):
    rota = [ponto_inicial] + list(i) + [ponto_inicial]  # Garantir que todas as rotas comecem e terminem em "R"
    acumulador_distancia = 0  # Inicializar o acumulador de distâncias para somar as distâncias
    for coordenada in range(len(rota) - 1):
        acumulador_distancia += distancias(pontos[rota[coordenada]], pontos[rota[coordenada + 1]])

    # Seleção da menor rota
    menor_rota = list(rotas.keys())
    # Se a distância acumulada da rota atual for menor que a menor distância armazenada, 
    # devo limpar o dicionário rotas e armazenar a nova menor distância e a rota correspondente
    if acumulador_distancia < int(menor_rota[0]):
        rotas.clear()
        rotas[acumulador_distancia] = rota

# Tirar o 'R' e formatar em uma única string visual
menor_rota_visual = list(rotas[min(rotas.keys())])
menor_rota_visual.remove("R")
if menor_rota_visual[-1] == ponto_inicial: # se o último caractere for "R", é só remover.
    menor_rota_visual.pop()

# Printar na tela a menor rota e a menor distância
print('=== FlyFood ===')
print('A menor rota é:')
print(" -> ".join(menor_rota_visual))
print(f'A menor distância é: {min(rotas.keys())}') # mostrar qual foi a menor distância encontrada.

# Verificar o tempo de Execução do Algoritmo
final = time.time()
print("Tempo de execução: ", final - inicial)
