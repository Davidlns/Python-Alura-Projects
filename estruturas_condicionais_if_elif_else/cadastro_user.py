while True:
    user = input('Digite seu nome de usuário: ')
    if len(user) < 5:
        print('O nome de usuário deve ter pelo menos 5 caracteres.')
    else:
         break

while True:
    passw = input('Digite sua senha: ')
    if len(passw) < 8:
        print('A senha deve ter pelo menos 8 caracteres.')
    else:
        break

print('Conta cadastrada com sucesso!')