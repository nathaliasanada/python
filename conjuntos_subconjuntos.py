conjunto = {1, 2, 3, 4, 5,}
conjunto2 = {5, 6, 7, 8}
conjunto_uniao = conjunto.union(conjunto2)
print('uniao: {}'.format(conjunto_uniao))
conjunto_interseccao = conjunto.intersection(conjunto2)
print('interseccao: {}'.format(conjunto_interseccao))
conjunto_diferenca1 = conjunto.difference(conjunto2)
print('diferença entre1 e 2 {}'.format(conjunto_diferenca1))
conjunto_diferenca2 = conjunto2.difference(conjunto)
print('diferença entre 2 e 1 {}'.format(conjunto_diferenca2))
conjunto_diferenca_simetrica = conjunto.symmetric_difference(conjunto2)
print('diferenca simetica: {}'.format(conjunto_diferenca_simetrica))

conjunto_a = {1, 2, 3}
conjunto_b = {1, 2, 3, 4, 5}
conjunto_subset = conjunto_a.issubset(conjunto_b)
print('a é subconjunto de b: {}'.format(conjunto_subset))
conjunto_superset = conjunto_b.issuperset(conjunto_a)
print('b é um superconjunto de a: {}'.format(conjunto_superset))

lista = ['cachorro', 'cachorro', 'gato', 'gato', 'elefante']
print(lista)
conjunto_animais = set(lista)
print(conjunto_animais)

lista_animais = list(conjunto_animais)
print(lista_animais)
