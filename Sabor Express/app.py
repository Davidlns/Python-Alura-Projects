import os

restaurantes = ['Bella Vista', 'Pé de fava', 'Sabor do Nordeste']

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
    os.system('cls')
    print('Finalizando o app\n')

def voltar_ao_menu():
    input('\nDigite uma tecla para voltar ao menu...')
    main()

def opcao_invalida():
    print('Opção Inválida!\n')

    voltar_ao_menu()

def exibir_subtitulo(subtitulo):
    os.system('cls')
    print(f'{subtitulo} \n')

def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastro de Restaurante:')
    nome_do_restautante = input('Digite o nome do restaurante que deseja cadastrar: ')
    restaurantes.append(nome_do_restautante)
    print(f'\nRestaurante {nome_do_restautante} foi cadastrado com sucesso!')

    voltar_ao_menu()

def listar_restaurantes():
    exibir_subtitulo('Lista de Restaurantes: ')
    if len(restaurantes) == 0:
        print('Nenhum Restaurante cadastrado.')

        voltar_ao_menu()
    else:
        for restaurante in restaurantes:
            print(f'{restaurante}')

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
                    print('Ativando Restaurante...')
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