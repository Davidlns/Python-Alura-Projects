while True:
    try:
        cord_x = float(input('Digite a cordenada X: '))
        cord_y = float(input('Digite a cordenada Y: '))

        if cord_x > 0 and cord_y > 0:
            print('Primeiro Quadrante')
        elif cord_x < 0 and cord_y > 0:
            print('Segundo Quadrante')
        elif cord_x < 0 and cord_y < 0:
            print('Terceiro Quadrante')
        elif cord_x > 0 and cord_y < 0:
            print('Quarto Quadrante')
        else: 
            print('O ponto está localizado no eixo ou origem!')

        break
    except(ValueError):
        print('Digite valores válidos')
