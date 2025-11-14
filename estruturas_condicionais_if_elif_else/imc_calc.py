peso = float(input('Digite seu peso: ').replace(',','.'))
altura = float(input('Digite sua altura: ').replace(',','.'))
calc_imc = peso / (altura ** 2)
print(calc_imc)

if calc_imc < 18.5:
    print('Abaixo do peso.')
elif calc_imc < 25:
    print('Peso normal.')
elif calc_imc < 30:
    print('Acima do peso.')
else:
    print('Obesidade')