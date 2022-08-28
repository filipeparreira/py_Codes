#Escreva um programa que converta uma temperatura digitando em graus Celsius e
# converta para graus Fahrenheit.

temp = float(input('Digite a temperatura em graus Celsius: '))
conv = (temp * (9/5)) + 32

print('A temperatura {:.1f}°C equivale a {:.1f}°F'.format(temp, conv))