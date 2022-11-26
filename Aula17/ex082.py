#Crie um programa que vai ler varios numeros e coloca-los em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores 
# pares e o valores impares digitados, respectivamente.
# Ao final, mostre o conteudo das três listas geradas.

valores, valores_i, valores_p = list(), list(), list()

while True:
    num = int(input('Digite um número: '))
    valores.append(num)

    op = str(input('Quer continuar? (S/N) ')).strip().upper()

    while op != 'S' and op != 'N':
        op = str(input('Opção inválida!! Digite S ou N: ')).strip().upper()
    
    if op == 'N':
        break

for item in valores:
    if (item % 2) == 0:
        valores_p.append(item)
    else:
        valores_i.append(item)

print('=-' * 30)
print(f'A lista completa é: {valores}')
print(f'A lista de pares é: {valores_p}')
print(f'A lista de impares é: {valores_i}')