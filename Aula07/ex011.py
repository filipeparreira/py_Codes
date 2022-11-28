#Faça um programa que leia a largura e a altura de uma parede em metros, calcule sua area e a
#quantidade de tinta necessaria para pinta-la, sabendo que cada litro de tinta pinta uma area de
#2 m²

h = float(input('Digite a altura da parede: '))
l = float(input('Digite a largura da parede: '))

a = l * h
qnt_t = a / 2

print('A área da parede é: {}m²\nE a quantidade de tinta necessaria para pinta-lá é: {}l'.format(a, qnt_t))