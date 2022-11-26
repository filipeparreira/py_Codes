#Crie um programa que vai ler vários numeros e colocar em uma lista.
# Depois disso mostre:
# - Quantos numeros foram digitados
# - Lista de valores ordenado de forma decrescente
# - Se o valor 5 foi digitado e está ou não na lista

count_numeros, valores, valor_5 = 0, list(), False

while True:
    num = int(input('Digite um valor: '))
    valores.append(num)

    op = str(input('Você quer continuar? (S/N) ')).strip().upper()

    while op != 'S' and op != 'N':
        op = str(input('Opção incorreta!!! Digite S ou N: ')).strip().upper()
    
    if num == 5:
        valor_5 = True
    
    count_numeros += 1
    
    if op == 'N':
        break

print('=-'*30)
print(f'Você digitou {count_numeros} elementos.')
print(f'Os valores em ordem decrescente são: {sorted(valores, reverse=True)}')

if valor_5:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não faz parte da lista!') 
