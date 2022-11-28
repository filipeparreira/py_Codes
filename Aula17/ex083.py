#Crie um programa onde o usuario digite uma expressão qualquer que use parenteses
# Seu aplicativo devará analisar se a expressão passada está com os parenteses abertos
# e fechados na ordem correta.

exp = str(input('Digite a expressão: '))

partentese_1 = exp.split('(')
partentese_2 = exp.split(')')

if len(partentese_1) == len(partentese_2):
    print('Sua expressão está correta!!')
else:
    print('Sua expressão está errada!!')
    