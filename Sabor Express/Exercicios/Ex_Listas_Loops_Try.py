#Criando Listas:
lista_numeros = [1,2,3,4,5,6,7,8,9,10]
lista_nomes = ['David', 'Nay', 'Stella', 'Ravi']
lista_ano = [2002, 2025]

def percorrer_lista():
    #Crie uma lista e utilize o loop for pra percorrer todos os elementos dela
    numeros = [3,2,1]
    for num in numeros:
        print(num)

def somar_impares():
    #Utilize um loop para calcular os numeros impares de 1 a 10:
    soma = 0
    for i in range(1, 11):
        if i % 2 == 1:
            soma += i
    print(soma)

def listar_descrecente():
    #Utilize o Loop for para imprimir os numeros de 1 a 10 em ordem decrescente
    for i in reversed(range(1, 11)):
        print(i)

def tabuada_input():
    #Solicite um numero e use loop para imprimir a tabuada de 1 a 10
    while True:
        try:
            numero = int(input('Digite um número: '))
            
            if numero > 0:
                mult = 1
                resultado = 0
                while mult <= 10:
                    resultado = numero * mult
                    print(f'{numero}x{mult}={resultado}')
                    mult += 1
                break
            else:
                print('Digite um número positivo...')

        except:
            print('Digite um número inteiro...')

def soma_lista():
    #Use loop para calcular a soma dos numeros de uma lista, use try-except para lidar com exceções
    numeros = [3, 4, 10, '1']
    soma = 0
    for numero in numeros:
        try:
            if isinstance(numero, int) or isinstance(numero, float):
                soma += numero
            else:
                print(f'\n( {numero} ) não é de tipos numéricos, tentaremos converter')
                soma += float(numero)
                print('Valor convertido com Sucesso!')
        except:
            print('Não foi possível converter, apenas números são aceitos na lista')
    print(f'\nA soma dos números presentes na lista é: {soma}\n')

soma_lista()