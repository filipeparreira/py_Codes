#Faça um programa que leia o ano de nascimento de um jovem e informe de acordo com sua idade:
#- Se ele ainda vai se alistar ao serviço militar
#- Se é a hora de se alistar
#- Se já passou do tempo do alistamento
#Seu programa também devera mostrar o tempo que falta ou se passou do prazo
from datetime import date

ano = int(input('Digite seu ano de nascimento: '))
idade = date.today().year - ano

if idade > 18:
    if idade - 18 == 1:
        print('ALERTA!! Já passou {} ano do alistamento, aliste-se imediatamente.'.format(idade - 18))
    else:
        print('ALERTA!! Já passou {} anos do alistamento, aliste-se imediatamente.'.format(idade - 18))
elif idade < 18:
    if 18 - idade == 1:
        print('Daqui à {} ano você terá que se alistar, fique atento!!'.format(18 - idade))
    else:
        print('Daqui à {} anos você terá que se alistar, fique atento!!'.format(18 - idade))
else:
    print('ALERTA!! Assim que possivel procure um posto de alistamento, está na hora, você tem {} anos.'.format(idade))
