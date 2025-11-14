#enunciado
'''Para números pares, exiba: "Faltam apenas <número> segundos - Não perca essa oportunidade!".
Para números ímpares, exiba: "A contagem continua: <número> segundos restantes.".
Ao final da contagem, exiba a mensagem: "Aproveite a promoção agora!".'''

numero_contagem = 10

while numero_contagem > 0:
    print(f'Faltam apenas {numero_contagem} segundos - Não perca essa oportunidade' if numero_contagem % 2 == 0 
          else f'A contagem continua: {numero_contagem} segundos restantes')
    
    numero_contagem -= 1

print('Aproveite a promoção agora!')
