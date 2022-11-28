#Refaça o desafio 009, mostrando a tabuada de um numero que o usuario escolher 
#só que agora utilizando um laço for 

num = int(input('Digite um numero inteiro para que possa ser mostrado sua tabuada: '))
print('TABUADA DO ', num)

for count in range(0, 11):
    print('{} x {} = {}'.format(num, count, num * count))