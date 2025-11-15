import os

opcoes_calculo = {
    "+": lambda x,y: x + y,
    "-": lambda x,y: x - y,
    "x": lambda x,y: x * y,
    "/": lambda x,y: x / y if y != 0 else 'Erro divisão por zero'
}

while True:
    try:
        os.system('cls')
        a = float(input('Digite o primeiro número: '))
        b = float(input('Digite o segundo número: '))
        op = input('Escolha um operador ( + | - | x | / ): ')

        if not op in {'+','-','x','/'}:
            print('Operador inválido! tente novamente com os operadores disponíveis')
            input('\ndigite qualquer tecla pra continuar...')
        else:
            break
    except(ValueError):
        print('\nSão aceitos apenas valores numéricos tente novamente')
        input('\ndigite qualquer tecla pra continuar...')

func = opcoes_calculo.get(op)

resultado = func(a,b)
print(f'\nO resultado é: {resultado}')

