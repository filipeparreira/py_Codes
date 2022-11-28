#Escreva um programa para aprovar o emprestimo bancario para compra de uma casa.
#O programa vai perguntar o valor da casa, o salario do comprador, e em quantos
#anos ele vai pagar.

#Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do
#salario, ou então o emprestimo será negado.

print('-*' * 20)
print('EMPRESTIMO BANCARIO')
print('-*' * 20)

valor_Casa = float(input('Digite o valor da casa (em R$): '))
sal_Comp = float(input('Digite o salario do comprador (em R$): '))
anos_Pag = float(input('Digite a quantidade de anos em que vai ser pago o emprestimo: '))

prest_Mensal = valor_Casa / (anos_Pag * 12)
porc_Sal = sal_Comp * 0.3

print('\nEm {} anos, a prestação será de R${:.2f}'.format(anos_Pag, prest_Mensal))

if prest_Mensal > porc_Sal:
    print('\nInfelizmente o banco não foi autorizado a fazer o empréstimo.')
    print('\nMotivo: Prestação mensal maior que 30% do salario do comprador.')
else:
    print('\nEmprestimo autorizado.')


