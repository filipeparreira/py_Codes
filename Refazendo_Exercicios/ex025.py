#Crie um programa que leia o nome de uma pessoa e diga se ela tem 'SILVA' no nome

nome = str(input('Digite um nome: ')).strip().upper()

print('Possiveis resultados:\nTrue - Contém SILVA no nome\nFalse - Não contém SILVA no nome')
print('Resultado: {}'.format('SILVA' in nome))