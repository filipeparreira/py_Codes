#Crie um programa que leia o nome e duas notas de varios alunos e guarde tudo em uma
# lista composta. No final, mostre um boletim contendo as médias de cada um e permita
# que o usuario possa mostrar as notas de cada aluno individualmente.

alunos = list()
count = 0

while True:
    alunos.append(list())
    nome = str(input('Nome: ')).capitalize().strip()
    alunos[count].append(nome)
    nota1 = float(input('Nota 1: '))
    alunos[count].append(nota1)
    nota2 = float(input('Nota 2: '))
    alunos[count].append(nota2)
    media = (nota1 + nota2) / 2
    alunos[count].append(media)

    op = str(input('Quer continuar? (S/N) ')).strip().upper()

    while op != 'S' and op != 'N':
        op = str(input('Opção incorreta!! DIGITE S ou N: '))
    
    count += 1

    if op == 'N':
        break

print('-='*20)
print(f'{"Nº":^4}{"Nome":^10}{"MÉDIA":^8}')
print('-'*22)

count = 0

for aluno in alunos:
    print(f'{count:^4}{aluno[0]:^10}{aluno[3]:^8.2f}')
    count += 1
print('-'*22)

while True:
    
    escolha = int(input('Mostrar nota de qual aluno?(999 Interrompe) '))

    while escolha >= len(alunos):
        escolha = int(input('Alunos não encontrado!! Digite outro aluno:(999 interrompe) '))
        if escolha == 999:
                break
    if escolha == 999:
        break

    print(f'As notas de {alunos[escolha][0]} são {alunos[escolha][1], alunos[escolha][2]}')

    print('-'*22)

    
    

        

