#Desenvolva um programa que leia seis numeros inteiros e mostre a soma apenas daqueles 
#que forem pares. Se o valor digitado for impar, desconsidere-o.

print('Digite seis numeros inteiros:')
total = 0

for count in range(0, 6):
    num = int(input('Numero {}: '.format(count + 1)))

    if num % 2 == 0:
        total += num

print('A soma dos numeros pares digitados é igual a: ', total)