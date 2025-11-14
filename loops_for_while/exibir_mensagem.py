'''Marcos está desenvolvendo um programa para exibir uma mensagem de boas-vindas repetidamente no console, 
como parte de uma campanha de marketing de sua plataforma chamada Buscante. Ele quer garantir que a mensagem seja exibida 5 vezes.
Ajude Marcos a escrever um programa que exiba a mensagem: "Bem-vindo ao Buscante!" o número exato de vezes que ele precisa.'''

mensagem_boasvindas = 'Bem vindo ao Buscante!'

#optei por usar while por ser um loop com numero de repetições conhecido e mais simples
contador = 0
while contador < 5:
    print(mensagem_boasvindas)
    contador += 1
