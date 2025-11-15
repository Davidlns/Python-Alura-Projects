def calcular_valores_separados():
    entrada = input('Informe os valores das vendas: ')
    nums = list(map(int, entrada.split()))
    soma = 0

    for num in nums:
        soma += num

    return soma

print(f'O total de vendas é de: R${calcular_valores_separados()}')