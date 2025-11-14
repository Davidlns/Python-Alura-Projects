atividade_A = int(input("Informe a quantidade de dias para a Atividade A: "))
atividade_B = int(input("Informe a quantidade de dias para a Atividade B: "))
atividade_C = int(input("Informe a quantidade de dias para a Atividade C: "))

if any (x < 0 for x in (atividade_A, atividade_B, atividade_C)):
    print("Valores negativos não são aceitos.")
else:
    calc_dias = atividade_A + atividade_B + atividade_C
    print(f'O tempo total das atividades são de {calc_dias} dias.')