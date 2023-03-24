a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))

if a > b and a > c:
    print('O Maior valor é {}'.format(a))
elif b > a and b > c:
    print('O maior valor é {}'.format(b))
else:
    print('O maior valor é {}'.format(c))    
print('Final do programa')