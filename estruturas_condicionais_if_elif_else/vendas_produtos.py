vendas_maca = int(input("Digite a quantidade de maçãs vendidas: "))
vemdas_banana = int(input("Digite a quantidade de bananas vendidas: "))

if vendas_maca > vemdas_banana: 
    print("As maçãs tiveram mais vendas.")
elif vendas_maca == vemdas_banana:
    print("Maçãs e bananas tiveram a mesma quantidade de vendas.")
else:
    print("As bananas tiveram mais vendas.")