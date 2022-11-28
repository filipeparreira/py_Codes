#Faça um programa que leia o peso de cinco pessoas, no final, mostre qual foi o maior
#e o menor peso lidos

maior = 0
menor = 0


for count in range(0, 5):
    peso = float(input('Digite o peso da pessoa {}: '.format(count + 1)))
    if count == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
    

print('O maior peso digitado foi: ', maior)
print('O menor peso digitado foi: ', menor)
