"""
------------------------------------------------------
PROJETO INTERDISCIPLINAR PARA SISTEMAS DE INFORMAÇÃO 2 
Nome: Yonara Mirely Araújo da Silva
Projeto: FlyFood
------------------------------------------------------
"""

# Gera todas as permutações possíveis de uma lista ou iterável.
from itertools import permutations

# É frequentemente usado como um valor inicial para comparações de mínimos e máximos.
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
        matriz.append(
            i.split()
        )  # Dividir cada elemento i de entrada pelo método split(), tendo por base os espaços e adicionar à lista 'matriz'.
    matriz.remove(matriz[0])  # Remover a primeira linha do arquivo pois não utilizarei

    # Localizar os pontos e as coordenadas
    for l in range(len(matriz)):  # Iterar sobre cada linha da matriz
        for c in range(len(matriz[0])):  # Número de elementos dentro da linha
            if matriz[l][c] != "0":  # Verifica se o elemento é 0 ou não
                pontos[matriz[l][c]] = [
                    l,
                    c,
                ]  # Adiciona no Dicionário a chave como ponto e o seu respectivo valor como coordenada

# print(pontos)


# Calcular as distâncias entre os pontos
def distancias(ponto1, ponto2):  # Recebe as coordenadas dos pontos
    # A distância de Manhattan é uma medida da distância entre dois pontos em uma grade baseada apenas em movimentos horizontais e verticais (não diagonais).
    # É a soma das diferenças absolutas de suas coordenadas, ou seja, X1-X2 + Y1-Y2.
    return abs((ponto1[0]) - (ponto2[0])) + abs((ponto1[1]) - (ponto2[1]))


# Permutando as rotas utilizando a biblioteca
permutações = permutations(pontos)

# for j in recebidos:
#     print(j) # todas as combinações

# Calcular todas as distâncias e encontrar a menor delas
distancia = []
# Dicionário para armezenar como chave a soma das distâncias de uma rota e o valor como a rota em si.
# Maxsize garante que qualquer rota válida seja menordo que a inicial
rotas = {maxsize: ("R", "D")}
# Cada permutação é uma rota potencial. O laço intera sobre todas as permutações possíveis dos pontos
for i in list(permutações):
    # Garantir que todas as rotas começem de "R"
    if i[0] == "R":
        for coordenada in range(len(i) - 1):
            distancia.append(
                distancias(pontos[i[coordenada]], pontos[i[coordenada + 1]])
            )
        # Voltando para o início = "R"
        # Após calcular as distâncias entre todos os pontos na permutação,
        # ele adiciona a distância do último ponto de volta ao ponto inicial "R".
        distancia.append(distancias(pontos[i[coordenada + 1]], pontos["R"]))

        # Seleção da menor rota
        # Converter as chaves de 'rotas' em uma lista para encontrar a menor rota
        menor_rota = list(rotas.keys())
        # Verificar se a soma das distâncias da rota atual é menor que a menor rota armazenada
        if sum(distancia) < int(menor_rota[0]):
            rotas.clear()  # Limpar o Dicionário
            rotas[sum(distancia)] = (
                i  # Adicionar a nova soma como chave e a nova rota como valor
            )

        distancia = []  # Limpar a lista para ser usada na próxima permutação

        # print(rotas)

# Tirar o 'R' e formatar em uma única string visual
menor_rota_visual = list(
    rotas[int(menor_rota[0])]
)  # Extrai a rota correspondente à menor soma de distâncias do dicionário rotas.
if "R" in menor_rota_visual:
    menor_rota_visual.remove("R")

# Printar na Tela a menor rota
print('=== FlyFood ===')
print('A menor rota é:')
print(" -> ".join(menor_rota_visual))
# Verificar o tempo de Execução do Algoritmo
final = time.time()
print("Tempo de execução: ", final - inicial)