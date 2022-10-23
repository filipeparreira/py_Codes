#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não
#com o nome 'SANTO'

cidade = str(input('Digite o nome de uma cidade: ')).strip().upper().split()

print('Possiveis resultados:\nTrue - O nome da cidade começa com SANTO\nFalse - O nome da cidade não começa com SANTO')
print('Resultado: {}'.format('SANTO' in cidade[0]))