#Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos
#de artifícios indo de 10 a 0, com uma pausa de 1 segundo entre eles
from time import sleep


print('FOGOS DE ARTIFICIOS!!')

for count in range(10, 0, -1):
    print(count)
    sleep(1)

print('Estorou!!')