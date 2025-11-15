def retornar_quantidade_caracteres():
    palavra = input('Digite uma palavra: ')
    qtde_caracteres = len(palavra)
    return f'Essa palavra tem {qtde_caracteres} caracteres'

print(retornar_quantidade_caracteres())


