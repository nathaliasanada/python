a = input("Digite um numero inteiro: ")
b = input("Digite um numero inteiro: ")
c = input("Digite um numero inteiro: ")

def verify_int(n):
    try:
        int(n)
        is_int = True
        return is_int
    except ValueError:
        is_int = False


if verify_int(a) and verify_int(b) and verify_int(c):
    a=int(a)
    b=int(b)
    c=int(c)
    print(a+b+c)
else:
    print('Você digitou alguma coisa que não é um número inteiro')
    