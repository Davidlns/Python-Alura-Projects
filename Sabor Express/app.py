import os

restaurantes = [{'nome':'Praça', 'categoria':'Japonesa', 'ativo':False},
                {'nome':'Pizza Suprema', 'categoria':'Pizza', 'ativo':True},                
                {'nome':'Cantina', 'categoria':'Italiano', 'ativo':False}]

def exibir_name_of_program():

    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
""")

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair\n')

def finalizar_app():
    exibir_subtitulo('Programa Finalizado...')

def voltar_ao_menu():
    input('\nDigite uma tecla para voltar ao menu...')
    main()

def opcao_invalida():
    print('Opção Inválida!\n')

    voltar_ao_menu()

def exibir_subtitulo(subtitulo):
    os.system('cls')
    linha = '*' * (len(subtitulo))
    print(linha)
    print(f'{subtitulo.upper()}')
    print(linha,'\n')

def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastro de Restaurante:')

    nome_do_restautante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite a categoria do restaurante {nome_do_restautante}: ')

    dados_do_restaurante = {'nome' : nome_do_restautante, 'categoria':categoria, 'ativo':False}
    restaurantes.append(dados_do_restaurante)

    print(f'\nRestaurante {nome_do_restautante} foi cadastrado com sucesso!')

    voltar_ao_menu()

def listar_restaurantes():
    exibir_subtitulo('Lista de Restaurantes: ')
    if len(restaurantes) == 0:
        print('Nenhum Restaurante cadastrado.')

        voltar_ao_menu()
    else:
        for restaurante in restaurantes:
            nome_restaurante = restaurante['nome']
            categoria_restaurante = restaurante['categoria']
            ativo = 'Ativado' if restaurante['ativo'] else 'Desativado'

            print(f'{nome_restaurante} | {categoria_restaurante} | {ativo}\n' )

        voltar_ao_menu()

def ativar_desativar_restaurante():
    exibir_subtitulo('Alternando estado do restaurante: ')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: \n')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_do_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            print(f'O restaurante {nome_do_restaurante} foi encontrado!\n')
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_do_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_do_restaurante} foi desativado com sucesso'
            print(f'\n{mensagem}\n')

    if not restaurante_encontrado:
        print(f'Restaurante {nome_do_restaurante} não encontrado!')
    voltar_ao_menu()


def escolher_opcao():
        try:
            opcao_escolhida = int(input('Escolha uma Opção: '))

            match opcao_escolhida:
                case 1:
                    cadastrar_novo_restaurante()
                case 2:
                    listar_restaurantes()
                case 3:
                    ativar_desativar_restaurante()
                case 4:
                    finalizar_app()
                case _:
                    opcao_invalida()

        except:
            opcao_invalida()
            

def main():
    exibir_name_of_program()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()