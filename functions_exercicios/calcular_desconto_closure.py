import os

os.system('cls')

desconto_porc = float(input('\nDigite a porcentagem de desconto: '))

def calcular_desconto(porc):
    valor_compra = float(input('\nDigite o valor da compra: '))
    def aplicar_desconto():
        calc = valor_compra - (valor_compra * (porc / 100))
        return calc
    
    return aplicar_desconto

fn = calcular_desconto(desconto_porc)
print(f"\n\nO valor final do produto é: {fn()}\n")        