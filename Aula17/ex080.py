#Crie um programa onde o usuario possa digitar cinco valores numericos e cadastre-os 
# em uma lista, já na posição correta de inserção (sem usar o sort()),
# no final mostre a lista ordenada na tela.

valores = list()

num = int(input('Digite um valor: '))
valores.append(num)

for count in range(0, 4):
    num = int(input('Digite outro valor: '))

    if num < valores[0]:
        valores.insert(0, num)
    elif num > valores[len(valores)-1]:
        valores.append(num)
    else:
        for count_aux in range(0, len(valores)):
            if num < valores[count_aux]:
                valores.insert(count_aux, num)
                break

print(valores)
        

