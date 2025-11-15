def juntar_produtos_precos():
    produtos = input('Digite os produtos separados por vírgula: ')
    precos = input('Digite os preços separados por vírgula: ')

    lista_produtos = [p.strip() for p in produtos.split(',')] #strip remove espaços extras
    lista_precos = [p.strip() for p in precos.split(',')] #split separa palavras por vírgula

    if len(lista_produtos) != len(lista_precos):
        raise ValueError('Quantidade de produtos e preços não coincidem')
    
    def to_float(x):
        x = x.replace(',','.') # aceita virgula decimal trocando pra .
        return float(x)

    lista_conjunta = []

    for prod, preco in zip(lista_produtos, lista_precos): #zip empacota elementos de duas sequencias em pares/tuplas
        lista_conjunta.append(f'{prod}: {to_float(preco):.2f}')

    def exibir_produtos(lista):
        for item in lista:
            print(f'\n{item}\n')

        return f'\n'

    return exibir_produtos(lista_conjunta)


print(juntar_produtos_precos())
