#Refaça o desafio 35 dos triangulos, acrescentando o recurso de mostrar que tipo de triangulo
#será formado.
#- Équilatero: Todos os lados iguais
#- Isóceles: Dois lados iguais
#- Escaleno: Todos os lados diferentes

r1 = float(input('Digite o comprimento de uma reta: '))
r2 = float(input('Digite o comprimento de outra reta: '))
r3 = float(input('Digite o comprimento de outra reta: '))
tri = False

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    tri = True

if tri == True:
    print('\nAs três retas formam um triangulo.')
    if r1 == r2 and r2 == r3 and r3 == r1:
        print('\nEste triangulo é um triangulo Équilatero.')
    elif r1 == r2 or r2 == r3 or r3 == r1:
        print('\nEste triangulo é um triangulo Isóceles.')
    elif r1 != r2 and r2 != r3 and r3 != r1:
        print('\nEste triangulo é um triangulo Escaleno.')
else:
    print('As três retas não formam um triangulo.')
