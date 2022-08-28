#Escreva um programa que pergunte o salario de seu funcionario e calcule o valor do seu aumento
#Para salarios superiores a R$1.250,00 calcule o aumento de 10%
#Para inferiores ou iguais o aumento é de 15%

sal = float(input('Digite seu salario: '))

print('Seu salario foi ajustado.')
if sal > 1250:
    aum = sal * 0.1
    print('O aumento do seu salario foi de 10%')
else:
    aum = sal * 0.15
    print('O aumento do seu salario foi de 15%')

print('Salario antigo: R${:.2f}'.format(sal))
print('Salario novo: R${:.2f}'.format(sal + aum))

