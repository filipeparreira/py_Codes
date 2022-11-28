#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. 
#No final, mostre os 10 primeiros termos dessa progressão

primeiro_termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))

print('Os 10 primeiros termor da PA de razão {} é: '.format(razao), end='')
for count in range(0, 11):
    print('{},'.format(primeiro_termo + (count * razao)), end=' ')