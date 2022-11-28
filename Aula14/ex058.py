#Melhore o jogo do desafio 028, onde o computador vai pensar em um numero entre 0 e 10.
#Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos
#palpites foram necessarios para vencer.

from random import randrange

jogador = int(input('Digite um numero entre 0 e 10: '))
comp = randrange(0, 10)
count = 0


while jogador != comp:
    if jogador < 0 or jogador > 10:
        print('Valor digitado fora dos limites de 0 a 10!!!')        
    count += 1
    print('Numero errado!!!')
    jogador = int(input('Digite outro numero entre 0 e 10: '))

print('Acertou o numero!!!!\nComp: {}\nJogador: {}\nQuantidade de tentativas: {}'.format(comp, jogador, count))

    