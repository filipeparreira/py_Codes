#Faça um programa que leia uma frase pelo teclado e mostre:
#- Quantas vezes aparece a letra 'A'
#- Em que posição ela aparece a primeira vez
#- Em que posição ela aparece a ultima vez

frase = str(input('Digite uma frase: ')).strip()

print('Na frase: {}\n--Aparece a letra [A]: {} vezes.\n--Sendo a primeira vez na {} posição.'.format(frase, frase.lower().count('a'), frase.lower().find('a') + 1))
print('--Sendo a ultima vez na {} posição.'.format(frase.lower().rfind('a') + 1))

