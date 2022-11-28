#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final
#do programa, mostre:
#- A média de idade do grupo
#- Qual o nome do homem mais velho
#- Quantas mulheres tem menos de 20 anos

media = 0
count_mulheres = 0

for count in range(0, 4):
    nome = str(input('Digite o nome da {}ª pessoa: '.format(count + 1))).strip().title()
    idade = int(input('Digite a idade da {}ª pessoa: '.format(count + 1)))
    sexo = str(input('Digite o sexo da {}ª pessoa (m / f): '.format(count + 1))).strip().lower()

    media += idade

    if count == 0:
        nome_velho = nome
        idade_velho = idade
    elif count < 3:
        if sexo ==  'm':
            if idade > idade_velho:
                nome_velho = nome
                idade_velho = idade
        if sexo == 'f':
            if idade < 20:
                count_mulheres += 1
    else:
        media = int(media / 3)

print('A idade média do grupo de pessoas é: ', media)
print('O nome do homem mais velho é: ', nome_velho)
print('{} mulheres tem menos de 20 anos.'.format(count_mulheres))    
    