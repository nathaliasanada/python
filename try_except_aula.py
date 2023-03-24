
# lista = [1, 10]
# try:
#     divisao = 10 / 0
#     numero = lista[1]

# except ZeroDivisionError:
#     print('Não é possivel realizar uma divisão por 0')
# except ArithmeticError:
#     print('Houve um erro ao realizar uma operação aritmetica')    
# except IndexError:
#     print('Erro ao acessar um indice invalido da lista')
# except Exception as ex:
#     print('erro desconhecido. erro: {}'.format(ex))  


class Error(Exception):
    pass

class InputError(Error):
    def __init__(self, message):
        self.message = message

while True:
    try:
        x = int(input('Digite a nota de 0 a 10: '))
        print(x)
        if x > 10:
            raise InputError('Não pode ser maior que 10')
        elif x < 0:
            raise InputError('Não pode ser menor que 0')
        break
    except ValueError:
        print('Valor invalido, digite apenas numeros: ')
    except InputError as ex: 
        print(ex)
