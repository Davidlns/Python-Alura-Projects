
#1 - Crie um dicionário representando informações sobre uma pessoa, como nome, idade e cidade.
dicionario = {'nome':'David Lins Amaral', 'Idade':25, 'cidade':'Los Angeles'}

#Modifique o valor de um dos itens no dicionário (por exemplo, atualize a idade da pessoa);
dicionario['Idade'] = 27
print(dicionario)

#Adicione um campo de profissão para essa pessoa
dicionario['Profissão'] = 'CEO'
dicionario['Segmento'] = 'Tec'
dicionario.update({'patrimônio':f'US$ 789.870.356,00'}) #segunda forma de adicionar itens ao dicionário
dicionario.update({'Empresa':f'Shark Code'})
print(dicionario)

#Remova um item do dicionário
dicionario.pop('Segmento') #para remover um item do dicionário
del dicionario['Empresa'] #segunda forma de remover
print(dicionario)

# Crie um dicionário que relacione os números de 1 a 5 aos seus respectivos quadrados.
quadrados = {1:1, 2:4, 3:9, 4:16, 5:25}
print(quadrados)

#Crie um dicionário e verifique se uma chave específica existe dentro desse dicionário
verificar = {'item1':'martelo','item2':'furadeira','item3':'machado'}

#VERIFICAÇÃO DE CHAVES
if 'item2' in verificar:#true chave existe
    print('A chave existe no dicionário')

if 'item6' not in verificar:#true chave não existe de acordo com not in que sugere negação
    print('A chave item6 não existe no dicionário')

print(f'item10' in verificar)##false chave não existe
print(f'item3' in verificar)##true chave existe

#VERIFICAÇÃO DE VALORES
print(f'martelo' in verificar.values())#verifica se um 'valor' existe dentro do dicionário


#Escreva um código que conte a frequência de cada palavra em uma frase utilizando um dicionário.
frase = 'Eu Vou Ser Multimilionário Um Dia'
frase = frase.lower() #transforma todas as letras de uma string em minúsculas
palavras = frase.split() #serve para criar uma lista separando todas as palavras presentes em uma frase
freq = {}

for p in palavras:
    freq[p] = freq.get(p, 0) + 1