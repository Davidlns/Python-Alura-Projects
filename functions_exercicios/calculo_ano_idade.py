ano_nascimento = int(input('Digite seu ano de nascimento: '))
ano_atual = int(input('Digite o ano atual: '))

def calcular_idade(ano_nascimento, ano_atual):
    idade = ano_atual - ano_nascimento
    print(f'A idade é {idade} anos')

calcular_idade(ano_nascimento, ano_atual)