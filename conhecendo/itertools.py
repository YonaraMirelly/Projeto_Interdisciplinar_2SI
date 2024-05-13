# from itertools import combinations
# lista = [1,2,3,4,5]
# combinacoes = list(combinations(lista, 3)) # o primeiro eh sempre uma lista e 
# # o segundo são quantos numeros eu vou querer dentro de cada combinação = LEMBRAR DE COLOCAR O LIST

# print(combinacoes)

from itertools import permutations
for i in permutations('abc'):
    print(i) # retorna todas as combinações possíveis com base na string