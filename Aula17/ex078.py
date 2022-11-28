# Faça um programa que leia 5 valores numericos e guarde-os em uma lista.
#  No final mostre qual foi o maior e o menor valor digitado e suas respectivas
#  posições na lista

valores = list()
num = int(input('Digite um numero inteiro: '))
valores.append(num)
for count in range(0, 4):
    num = int(input('Digite outro numero inteiro: '))
    valores.append(num)

maior = valores[0]
posi_maior = list()
posi_menor = list()
menor = maior

for posi, num in enumerate(valores):
    if num > maior:
        maior = num
    if num < menor:
        menor = num

for posi, num in enumerate(valores):
    if num == maior:
        posi_maior.append(posi)
    if num == menor:
        posi_menor.append(posi)

print(f'O maior valor é {maior}.\nO menor valor é {menor}.')
print(f'O valor {maior} está nas posições: ', end='')
for num in posi_maior:
    print(f'{num}...', end='')
print(f'\nO valor {menor} está nas posições: ',end='')
for num in posi_menor:
    print(f'{num}...',end='')
print('\n')
    