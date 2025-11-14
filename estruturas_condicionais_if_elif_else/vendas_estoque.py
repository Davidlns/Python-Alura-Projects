qtde_produto = 5
i = 0

while qtde_produto > 0:
    qtde_produto -= 1
    print(f'Venda realizada! estoque restante: {qtde_produto}')
else:
    print('Estoque esgotado')