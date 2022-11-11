#Faça um programa que leia o sexo de uma pessoa, mas só aceite valores
#'M' ou 'F'. Caso esteja errado, peça a resposta novamente até ter um valor correto

sexo = str(input('Digite o seu sexo [M/F]: ')).upper().strip()

if sexo != 'M' and sexo != 'F':
    while sexo != 'M' and sexo != 'F':
        print('Valor incorreto!!')
        sexo = str(input('Digite o seu sexo [M/F]: ')).upper().strip()
        print(sexo)

print('Valor correto!')