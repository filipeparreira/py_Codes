#Aprimore o desafio anterior, mostrando no final:
# - A soma de todos os valores pares digitados
# - A soma dos valores da terceira coluna
# - O maior valor da segunda linha

matriz = [list(), list(), list()]
soma_p = soma_coluna = maior = 0 

for c in range(0, 3):
    for count in range(0, 3):
        num = int(input(f'Digite um valor para [{c}, {count}]: '))
        matriz[c].append(num)
        if (num % 2) == 0:
            soma_p += num

print('-='*30)
print('MATRIZ:')
for linha in matriz:
    print(f'[{linha[0]}]    [{linha[1]}]    [{linha[2]}]')
    soma_coluna += linha[2]
print('-='*30)

print(f'A soma de todos os elementos pares da matriz é: {soma_p}.')
print(f'A soma de todos os elementos da terceira coluna é: {soma_coluna}.')
for item in matriz[1]:
    if item > maior:
        maior = item
print(f'O maior valor da segunda linha é {maior}.')