#Faça um programa que calcule a soma entre todos os numeros impares que são multiplos de 3
#e que se encontram no intervalo de 1 até 500

resultado = 0

for count in range(1, 501):
    if count % 2 != 0:
        if count %  3 == 0:
            resultado += count

print('A soma de todos os numeros impares e multiplos de 3, entre 1 e 500 é: ', resultado)