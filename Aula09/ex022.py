#Crie um programa que leia o nome completo de uma pessoa e mostre:
#-O nome completo com todas as letras maiusculas
#-O nome com todas as letras minusculas
#-Quantas letras ao to do ( sem considerar espaços)
#-Quantas letras tem o primeiro nome

nome = input('Digite seu nome completo: ').strip()
nome_m = nome.upper()
nome_n = nome.lower()
nome_se = len(nome) - nome.count(' ')
nome_sp = nome.split()
nome_p = len(nome_sp[0])

print('Nome com todas letras maiusculas: {}'.format(nome_m))
print('Nome com todas letras minuscuas: {}'.format(nome_n))
print('Sem os espaços, o nome tem: {} letras.'.format(nome_se))
print('O primeiro nome tem: {} letras.'.format(nome_p))
