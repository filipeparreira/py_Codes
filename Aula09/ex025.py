#Crie um programa que leia o nome de uma pessoa e diga se ela tem 'Silva' no nome

nome = str(input('Digite o nome: ')).strip().lower()

print('Analisando nome...')
print('No nome digitado tem o nome Silva?\n\n   {}'.format('silva' in nome))