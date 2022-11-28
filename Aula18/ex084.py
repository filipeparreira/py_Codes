#Faça um programa que leia o nome e o peso de varias pessoas, guardando tudo em uma lista.
# No final, mostre:
# - Quantas pessoas foram cadastradas 
# - Uma listagem com as pessoas mais pesadas
# - Uma listagem com as pessoas mais leves
# Obs.: 70 Kg ou menos são pessoas leves, 100 Kg ou mais são pessoas mais pesadas

pessoas = list()
pessoa = list()
pesados = list()
leves = list()
count_pessoas = 0

while True:
    pessoa.append(str(input('Nome: ')).strip())
    pessoa.append(float(input('Peso: ')))
    pessoas.append(pessoa.copy())
    pessoa.clear()

    count_pessoas += 1

    op = str(input('Quer continuar? (S/N) ')).strip().upper()

    while op != 'S' and op != 'N':
        op = str(input('Opção invalida!! Digite S ou N: ')).strip().upper()

    if op == 'N':
        break

maior = menor = pessoas[0][1]

for pessoa in pessoas:
    if pessoa[1] >= maior:
        maior = pessoa[1]
    elif pessoa[1] <= menor:
        menor = pessoa[1]

for pessoa in pessoas:
    if pessoa[1] == maior:
        pesados.append(pessoa.copy())
    if pessoa[1] == menor:
        leves.append(pessoa.copy())

print('-='*30)
print(f'Ao todo, você cadastrou {count_pessoas} pessoas.')
print(f'O maior peso foi de {maior}. Peso de ', end='')
for pessoa in pesados:
    print(pessoa[0], end=', ')
print(f'\nO menor peso foi de {menor}. Peso de ', end='')
for pessoa in leves:
    print(pessoa[0], end=', ')
print('\n')




