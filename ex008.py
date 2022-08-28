#Escreva um programa que leia um valor em metros e exiba um resultado em centimetros e
#um em milimetros

metros = float(input('Digite um valor em metros: '))
cem = metros * 100
mili = metros * 1000

print('{} metros corresponde a {} centimetros'.format(metros, cem))
print('{} metros corresponde a {} milimetros'.format(metros, mili))
