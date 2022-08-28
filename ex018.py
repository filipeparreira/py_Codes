#Faça um programa qualquer que leia um angulo qualquer e mostre na tela
#o valor do seno cosseno e tangente desse angulo

from math import sin, cos, tan, radians
ang = float(input('Digite o ângulo: '))
rang = radians(ang)
c = cos(rang)
s = sin(rang)
t = tan(rang)

print('O seno de {:.2f}º é {:.2f}\nO cosseno de {:.2f}º é {:.2f}'.format(ang, s, ang, c))
print('A tangente de {:.2f}º é {:.2f}'.format(ang, t))
