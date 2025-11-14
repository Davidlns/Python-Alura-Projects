renda_mensal = float(input('Informe o valor da sua renda mensal: ').replace(',','.'))
valor_parcela = float(input('Digite o valor da parcela desejada: ').replace(',','.'))
porc_30 = renda_mensal * 0.3

#condições para emprestimo
renda_aceita = renda_mensal > 2000
parcela_aceita = valor_parcela <= porc_30

if renda_aceita and parcela_aceita:
    print('Emprestimo Aprovado!')
elif not renda_aceita:
    print('Emprestimo negado: Renda deve ser maior que 2000.')
else:
    print('Emprestimo negado: valor da parcela maior que 30% da renda')