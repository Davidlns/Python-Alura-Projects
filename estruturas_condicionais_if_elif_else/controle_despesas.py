limite = 3000
despesas_mes = float(input('Digite o total de despesas do mês: ').replace(',','.'))

if despesas_mes > limite:
    print('Atenção! Você ultrapassou o limite do orçamento.')
else:
    print('Sua despesa está dentro do limite.')