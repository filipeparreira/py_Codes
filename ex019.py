#Um professor quer sortear um de seus 4 alunos para apagar o quadro.
#Faça um programa que ajude ele, lendo os nomes deles e escrevendo o nome escolhido.

from random import choice
n0 = input('Digite o nome de um aluno: ')
n1 = input('Digite o nome de outro aluno: ')
n2 = input('Digite o nome de outro aluno: ')
n3 = input('Digite o nome de outro aluno: ')

n = choice([n0, n1, n2, n3])

print('O aluno escolhido foi: {}'.format(n))





