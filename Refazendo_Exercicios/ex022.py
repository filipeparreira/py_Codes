#Crie um programa que leia o nome completo de uma pessoa e mostre:
#   - O nome com todas as letras maiusculas
#   - O nome com todas as letras minusculas
#   - Quantas letras tem ao todo, sem considerar os espaços
#   - Quantas letras tem o primeiro nome

nome = str(input('Digite um nome: ')).strip().title()
nome_m = nome.upper()
nome_n = nome.lower()
nome_len = len(nome.replace(' ', ''))
nome_lista = nome.split()
nome_len_p = len(nome_lista[0])

print('\nNome: {}'.format(nome))
print('O nome com todas as letras maiusculas: {}'.format(nome_m))
print('O nome com todas as letras minusculas: {}'.format(nome_n))
print('Quantidade de letras que tem o nome, desconsiderando os espaços: {}'.format(nome_len))
print('Quantidade de letras que tem somente o primeiro nome: {}'.format(nome_len_p))