#Faça um programa que leia o nome completo de uma pessoa e mostre em seguida o primeiro
#e o ultimo nome separadamente
#Ex.: Ana Maria de Souza
#primeiro: Ana
#ultimo: Souza

nome = str(input('Digite seu nome completo: ')).strip().title()
lista = nome.split()
tl = len(lista)
print('Nome: {}\nPrimeiro nome: {}\nUltimo nome: {}'.format(nome, lista[(tl - tl)], lista[tl - 1]))

