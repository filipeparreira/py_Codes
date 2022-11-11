#Faça um programa que jogue par ou ímpar com o computador. O jogo será interrompido
#quando o jogador perder, mostrando o total de vitorias consecutivas que ele conquistou
#no final do jogo.

from random import randrange

msg = 'VAMOS JOGAR PAR OU ÍMPAR'
print('-+'*20)
print(f'{msg:^20}')
count = 0

while True:
    jogador = int(input('Diga um valor: '))
    pc = randrange(0, 10)
    op_jogador = str(input('Par ou Ímpar? [P/I] ')).upper().strip()

    while op_jogador != 'P' and op_jogador != 'I':
        print('OPÇÃO INCORRETA!!!')
        op_jogador = str(input('Par ou Ímpar? [P/I] ')).upper().strip()
    
    res = jogador + pc

    if op_jogador == 'P':
    
        if (res % 2) != 0:
            print('--'*20)
            print(f'Você jogou {jogador} e o computador jogou {pc}. Total de {res} DEU ÍMPAR')
            print('--'*20)
            print('Você PERDEU!!')
            print('-+'*20)
            break

        else:
            print('--'*20)
            print(f'Você jogou {jogador} e o computador jogou {pc}. Total de {res} DEU PAR')
            print('--'*20)
            print('Você GANHOU!!')
            print('-+'*20)
            count += 1
    
    if op_jogador == 'I':
        
        if (res % 2) == 0:
            print('--'*20)
            print(f'Você jogou {jogador} e o computador jogou {pc}. Total de {res} DEU PAR')
            print('--'*20)
            print('Você PERDEU!!')
            print('-+'*20)
            break
        else:
            print('--'*20)
            print(f'Você jogou {jogador} e o computador jogou {pc}. Total de {res} DEU ÍMPAR')
            print('--'*20)
            print('Você GANHOU!!')
            print('-+'*20)
            count += 1
        


print(f'GAME OVER! Você venceu {count} vezes.')