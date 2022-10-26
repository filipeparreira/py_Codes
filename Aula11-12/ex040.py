#Crie um programa que leia duas notas de um aluno e calcule sua media, mostrando uma mensagem no
#final de acordo com a média atingida.
#- Média abaixo de 5.0: Reprovado
#- Média média entre 5.0 e 6.9: Recuperação
#- Média 7.0 ou superior: Aprovado

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2

if media < 5.0:
    print('Sua média foi: {:.1f}\nSituação: REPROVADO'.format(media))
elif media > 5.0 and media < 6.9:
    print('Sua média foi: {:.1f}\nSituação: RECUPERAÇÃO'.format(media))
elif media >= 7.0:
    print('Sua média é: {:.1f}\n Situação: APROVADO'.format(media))