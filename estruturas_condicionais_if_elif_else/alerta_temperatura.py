temperatura = float(input('Digite a temperatura atual: '))
temp = str(temperatura).replace('.', ',')

if temperatura > 25:
    print(f'ALERTA!!!! A TEMPERATURA {temp}°C ESTÁ ACIMA DO LIMITE PERMITIDO.')
else:
    print(f'Temperatura {temp} é segura.')