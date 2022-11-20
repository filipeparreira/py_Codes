#Crie um programa que tenha uma tupla unica com nome de produtos e seus respectivos
#preços na sequencia.
#No final mostre uma listagem de preços organizando os dados em forma tabular

listagem = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.9, 'Estojo', 25, 'Transferidor', 4.20,
'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.9)

titulo = 'Listagem de Preços'
print('-'*40)
print(f'{titulo:^40}')
print('-'*40)

for count in range(0, len(listagem), 2):
    print(f'{listagem[count]:.<30}R${listagem[count+1]:.2f}')