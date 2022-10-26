#Crie um programa que faça o computador jogar Jokenpô com você

from random import randrange

print('#-#' * 20)
print('JOKENPÔ GAME')
print('#-#' * 20)
print('Escolha uma das opções:\n1. Pedra\n2. Papel\n3. Tesoura')
escolha_User = int(input())
escolha_Maqui = randrange(1, 4)




