#O mesmo professor anterior quer sortear a ordem de apresentação de trabalho dos alunos
#Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada

from random import shuffle

n0 = input('Digite o nome de um aluno: ')
n1 = input('Digite o nome de outro aluno: ')
n2 = input('Digite o nome de outro aluno: ')
n3 = input('Digite o nome de outro aluno: ')
alunos = [n0, n1, n2, n3]
shuffle(alunos)
print('A sequencia de alunos que iram apresentar o trabalho é: ')
print(alunos)

