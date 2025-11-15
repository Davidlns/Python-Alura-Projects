def identificar_saudacao():
    hora_atual = int(input('Digite a hora atual (0-23): '))

    if hora_atual < 12 and hora_atual > 0:
        print('Bom dia !')
    elif hora_atual < 18:
        print('Boa tarde!')
    else:
        print('Boa noite!')

identificar_saudacao()
