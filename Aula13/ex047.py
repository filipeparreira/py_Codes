#Crie um programa que mostre na tela todos os numeros pares que estão no intervalo
#entre 1 e 50

print('Todos numeros pares que estão em um intervalo entre 1 e 50: ', end='')

for count in range(1, 51):
    if count % 2 == 0:
        print(count, end=' ')