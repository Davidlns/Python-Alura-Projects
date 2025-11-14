livros = ["1984", "Dom Casmurro", "O Pequeno Príncipe", "O Hobbit", "Orgulho e Preconceito"]

nome_livro = input('Digite o nome do Livro que deseja buscar: ')
livro_encontrado = False

for livro in livros:
    if livro.casefold() == nome_livro.casefold():
        print(f'O livro {livro} foi encontrado')
        livro_encontrado = True
        break

if not livro_encontrado:
    print(f'O livro {nome_livro} não foi encontrado!')