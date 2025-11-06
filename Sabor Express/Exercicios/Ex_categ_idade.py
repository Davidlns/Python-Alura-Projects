def Perguntar_idade():
    while True:
        try:
            idade_usuario = int(input('Digite sua idade: '))
            return idade_usuario
        except ValueError:
            print('por favor, digite um número inteiro válido.')

def Definir_categoria_idade():

    idade = Perguntar_idade()

    if 0 < idade <= 12:
        print('Você é da categoria criança')
    elif 12 < idade <= 18:
        print('Você é adolescente')
    elif idade > 18:
        print('Você é adulto')
    else: 
        print('Idade inválida')

Definir_categoria_idade()