#Crie um programa que leia varios numeros inteiros pelo teclado, o programa só
#vai parar quando o usuario digitar o valor 999, que é a condição de parada
#no final mostre quantos numeros foram digitados e qual foi a soma entre eles.

num = int(input('Digite um valor [999 p/ parar]: '))
count = soma = 0

if num != 999:
    while True:
        count += 1
        soma += num

        num = int(input('Digite um valor [999 p/ parar]: '))
        if num == 999:
            break

print(f'A soma dos {count} valores foi {soma}!!')