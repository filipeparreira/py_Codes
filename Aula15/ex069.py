#Crie um programa que leia a idade e o sexo de varias pessoas. A cada pessoa cadastrada
#o programa deve perguntar se o usuario quer ou não continuar, no final mostre:
#a) Quantas pessoas tem mais de 18 anos.
#b) Quantos homens foram cadastrados.
#c) Quantas mulheres tem menos de 20 anos.

count_18 = count_m = count_20 = 0
msg = 'CADASTRE UMA PESSOA'

while True:
    print('-' * 20)
    print(f'{msg:^20}')
    
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F] ')).upper().strip()
    
    while sexo != 'M' and sexo != 'F':
        print('Sexo Inválido!!')
        sexo = str(input('Sexo: [M/F] ')).upper().strip()

    print('-' * 20)

    op = str(input('Deseja continuar? [S/N] ')).upper().strip()

    while op != 'S' and op != 'N':
        print('Opção Inválida!!')
        op = str(input('Deseja continuar? [S/N] ')).upper().strip()

    if idade > 18:
        count_18 += 1

    if idade < 20 and sexo == 'F':
        count_20 += 1
    
    if sexo == 'M':
        count_m += 1

    if op == 'N':
        break

print('=========FIM DO PROGRAMA=========')
print(f'Total de pessoas com mais de 18 anos: {count_18}.')
print(f'Ao todo temos {count_m} homens cadastrados.')
print(f'E temos {count_20} mulheres com menos de 20 anos.')





    