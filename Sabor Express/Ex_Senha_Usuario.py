usuario_cad = "user01"
senha_cad = "user2025@"

while True: 
    input_user = input("Nome de usuário: ")
    input_pass = input('Senha: ')

    if input_user == usuario_cad and input_pass == senha_cad:
        print('Usuário logado com sucesso!')
        break
    else:
        print('Usuário ou senha incorretos!')