#Crie um programa que tenha uma tupla totalmente preenchida
# com uma contagem por extenso, de zero até vinte.
# Se programa deverá ler um numero pelo teclado, entre 0 e
# 20 e mostrá-lo por extenso.

numeros = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
'Onze', 'Doze', 'Treze', 'Quartoze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte') 

num = int(input('Digite um numero de 0 até 20: '))

while True:
    if num < 0 or num > 20:
        num = int(input('O numero digitado não está no intervalo de 0 a 20.\nDigite novamente: '))
    else:
        break

print(f'Numero digitado só que por extenso: {numeros[num]}')