lista = [1, 3, 5, 7]
lista_animal = ['cachorro' , 'gato', 'elefante']
# print(lista_animal[1]) 

# print(sum(lista))
# print(max(lista))
# print(min(lista))

if 'lobo' in lista_animal:
    print('Existe um gato na lista')
else:
    print('Não existe um lobo na lista, sera incluido')
    lista_animal.append('lobo')
    print(lista_animal)

lista.sort()
print(lista)
lista_animal.sort()
print(lista_animal)

lista.reverse()
print(lista)
lista_animal.reverse()
print(lista_animal)

# lista_animal.pop()
# print(lista_animal)

# lista_animal.remove('elefante')
# print(lista_animal)


lista_animal [0] = 'tartaruga'
print(lista_animal)

tupla = (1, 10, 12, 14)
print(len(tupla))
print(len(lista_animal))
tupla_animal = tuple(lista_animal)
print(type(tupla_animal))
print(tupla_animal)
lista_numerica = list(tupla)
print(type(lista_numerica))
lista_numerica[0] = 100
print(lista_numerica)


