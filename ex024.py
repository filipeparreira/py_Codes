#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome SANTO.

cidade = str(input('Digite o nome da cidade: ')).strip().lower()
lista = cidade.split()
veri = 'santo' in lista[0]

print('Verificando nome...')
print('O nome da cidade digitada começa com Santo? \n\n  {}'.format(veri))
