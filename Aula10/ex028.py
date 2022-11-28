#Escreva um programa que faça um computador "pensar" em um numero de 0 a 5 e peça o usuario
#para tentar descobrir qual foi o numero escolhido pelo computador.
#O programa devera escrever na tela se o usuario venceu ou perdeu

from random import randrange

num = int(input('Digite um numero de 0 a 5: '))
comp = randrange(0, 5)

print('Processando o numero......\nComparando com o numero pensado pelo computador.....\n')

if num == comp:
    print('Você venceu!!! Conseguiu acertar o numero que o computador pensou!!!')
else:
    print('Você perdeu, o numero que o computador pensou é: {}'.format(comp))


