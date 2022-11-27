#Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo
# teclado. No final, mostre na tela com a formatação correta.

matriz = [list(), list(), list()]

for c in range(0, 3):
    for count in range(0, 3):
        matriz[c].append(int(input(f'Digite um valor para [{c}, {count}]: ')))
    
for linha in matriz:
    print(f'[{linha[0]}]    [{linha[1]}]    [{linha[2]}]')
    
    
