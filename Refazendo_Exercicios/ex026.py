#Faça um programa que leia uma frase pelo teclado e mostre:
#   - Quantas vezes aparece a letra 'a'
#   - Em que posição ela aparece a primeira vez
#   - Em que posição ela aparece a ultima vez

frase = str(input('Digite uma frase: ')).strip()

print('Quantidade de vezes em que aparece a letra (a): {}'.format(frase.count('a')))
print('A posição da primeira vez em que a letra (a) aparece: {}'.format(frase.find('a')))
print('A posição da primeira vez em que a letra (a) aparece: {}'.format(frase.rfind('a')))