#A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um
#atleta e mostre sua categoria de acordo com a idade.
#- Até 9 anos: Mirim
#- Até 14 anos: Infantil
#- Até 19 anos: Junior
#- Até 20 anos: Sênior
#-Acima: Master
from datetime import date
ano = int(input('Digite o ano do nascimento do atleta: '))
idade = date.today().year - ano

if idade <= 9:
    print('O atleta tem {} anos, logo faz parte da categoria Mirim.'.format(idade))
elif idade > 9 and idade <= 14:
    print('O atleta tem {} anos, logo faz parte da categoria Infantil.'.format(idade))
elif idade > 14 and idade <= 19:
    print('O atleta tem {} anos, logo faz parte da categoria Junior.'.format(idade))
elif idade > 19 and idade <= 20:
    print('O atleta tem {} anos, logo faz parte da categoria Sênior.'.format(idade))
else:
    print('O atleta tem {} anos, logo faz parte da categoria Master.'.format(idade))
