#Faça um algoritmo que leia um salario de um funcionario e mostre seu salario com 15% de aumento

sal = float(input('Digite seu salário atual: '))
aum = sal + (sal * 0.15)

print('Seu novo salario, com 15% de aumento é: R${:.2f}'.format(aum))