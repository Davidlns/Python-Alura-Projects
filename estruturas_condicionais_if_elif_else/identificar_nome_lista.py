projetos = ["website", "jogo", "análise de dados", None, "aplicativo móvel"]
print('\n')

for projeto in projetos:
    print(f'{projeto}' if projeto is not None else f'Projeto ausente')