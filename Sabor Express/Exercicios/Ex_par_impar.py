numero = int(input('Digite um número: '))

def par_impar(numero):
    match numero % 2:
        case 0:
            print('O numero é par')
        case _: 
            print('O numero é impar!')

par_impar(numero)
