"""
#Media Aritimética 

x = [10, 60, 360]

media = sum(x) / len(x)
print('Média: {}'.format(media))

#Media aritimética ponderada 
soma(dados * peso) / soma(peso)

pesos = [1, 2, 3, 4]
notas = [8, 7, 9, 9] 

notasXpesos = [notas[i]* pesos[i] for i in range(0, len(notas))]
media_pond = sum(notasXpesos) / sum(pesos)
print('Media ponderada: {}'.format(media_pond))
"""

# Média Harmonica Ponderada

x = [10,60,360]
y = [2, 2, 2, 2]

# Calculo manual
nx = len(x)
somaX = (1 / x[0]) + (1 / x[1]) + (1 / x[2])
print(f'Media harmonica = {nx} / {somaX:.4f}')
xh = nx / somaX
print(f'Média harmonica = {xh:.4f}')

#Calculo com loop 
somaX = [(1 / x[k])for k in range(0, len(x))]
somaX = sum(somaX)
xh = nx / somaX
print('Media Harmonica = {}'.format(xh))






