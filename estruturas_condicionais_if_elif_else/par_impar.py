try:
    numero_inteiro = int(input('Digite um numero inteiro: '))
    print(f'O numero {numero_inteiro} é par.' if numero_inteiro % 2 == 0 else f'O numero {numero_inteiro} é impar.')
except:
    print('O dado inserido é inválido, deve digitar um numero inteiro.')