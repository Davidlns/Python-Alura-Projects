distancia_km = float(input('Digite a distancia percorrida (Km): '))

if distancia_km <= 100:
    print('R$10,00')
elif distancia_km <= 200:
    print('R$20,00')
else:
    print('R$30,00')