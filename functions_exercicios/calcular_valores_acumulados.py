import os
os.system('cls')

def calcular_valores():
    while True:
        os.system('cls')
        try:
            numero = int(input('Digite um numero inteiro: '))
            contador = 1
            soma = 0

            while contador <= numero:
                soma += contador
                contador += 1

            break

        except(ValueError):
            print('\nValor digitado é inválido! Digite um valor inteiro\n')
            input('Digite qualquer tecla para tentar novamente...')

    return f'\nA soma de {1} a {numero} é: {soma}\n'

print(calcular_valores())