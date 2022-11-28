#Faça um programa que mostre a tabuada de varios numeros, um de cada vez,
#para cada valor digitado pelo usuario. O programa será interrompido quando
#o numero digitado for negativo

while True:
    num = int(input('Quer tabuada de qual valor? '))
    if num < 0:
        break
    print('-' * 20)
    for mult in range(1, 11):
        print(f'{num} x {mult} = {num * mult}')
    print('-' * 20)
    
print('Programa TABUADA encerrado!! Volte sempre!!')
