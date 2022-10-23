#Faça um programa que leia o nome completo de uma pessoa e em seguida mostre separadamente
#o primeiro e o ultimo nome dessa pessoa

nome = str(input('Digite um nome: ')).strip().title()
nome_l = nome.split()

print('Nome: {}'.format(nome))
print('Primeiro: {}'.format(nome_l[0]))
print('Ultimo: {}'.format(nome_l[len(nome_l) - 1]))