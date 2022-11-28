#Faça um programa que ajude um jogador da mega sena a criar palpites.
# O programa vai perguntar quantos jogos seram gerados e vai sortear 
# 6 numeros entre 1 e 60, para cada jogo, cadastrando em uma lista 
# composta.

from time import sleep
from random import randint

titulo = 'JOGUE NA MEGA SENA'
jogos = list()
palpites = list()

print('-#'*20)
print(f'{titulo:^40}')
print('-#'*20)

qntd_jogos = int(input('Quantos jogos você quer que eu sorteie? '))

for count in range(0, qntd_jogos):
    jogos.append(list())
    for count_aux in range(0, 6):
        num = randint(1, 60)
        while num not in jogos[count]:
            jogos[count].append(num)

print(f'-=-=-=-= SORTEANDO {qntd_jogos} JOGOS -=-=-=-=')
count = 1
for jogo in jogos:
    print(f'Jogo {count}: {jogo}')
    count += 1
    sleep(1)
print('-=-=-=-=-= < BOA SORTE!! > -=-=-=-=-=')



