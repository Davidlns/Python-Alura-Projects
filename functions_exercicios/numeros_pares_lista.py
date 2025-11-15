def retornar_pares():
    numeros_input = input('Digite os numeros separados por espaço: ')
    lista = list(map(int, numeros_input.split()))
    lista_pares = []

    for numero in lista:
        if numero % 2 == 0:
            lista_pares.append(numero)
    
    return lista_pares

pares = retornar_pares()
print('Números pares:', " ".join(map(str, pares)))
