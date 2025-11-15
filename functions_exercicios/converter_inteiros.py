telefones = ["11987654321", "21912345678", "31987654321", "11911223344"] 

def converter_inteiros(lista):
    lista_inteiros = []
    for item in lista:
        lista_inteiros.append(int(item))
    
    return lista_inteiros

def verificar_inteiros(lista):
    nao_inteiros = 0
    for item in lista:
        if type(item) != int:
            nao_inteiros += 1
            print(item, 'Não é do tipo inteiro')
    if nao_inteiros == 0:
        print('\n',lista)
        print('Todos os dados da lista são inteiros.\n')
    else:
        print('A lista tem dados que não são do tipo inteiro.\n')

verificar_inteiros(converter_inteiros(telefones))

verificar_inteiros(telefones)

