#Desenvolva um programa que leia o comprimento de três retas e diga ao usuario se elas podem
#ou não formar um triangulo

r1 = float(input('Digite o comprimento de uma reta: '))
r2 = float(input('Digite o comprimento de outra reta: '))
r3 = float(input('Digite o comprimento de outra reta: '))
tri = False

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    tri = True

if tri == True:
    print('As três retas formam um triangulo.')
else:
    print('As três retas não formam um triangulo.')
