#Escreva um programa que leia a velocidade de um carro.
#Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado
#A multa vai custar R$7,00 para cada Km acima do limite

vel = float(input('Digite a velocidade do carro (em Km/h): '))

if vel > 80.0:
    velf = vel - 80
    multa = velf * 7.0
    print('VOCÊ FOI MULTADO!!\nLimite de velocidade: 80 Km/h\nVelocidade em que você estava: {} Km/h'.format(vel))
    print('O valor total da multa a ser paga é de: R${:.2f}'.format(multa))
    print('Sendo que foi cobrado R$7.00 para cada Km ultrapassado do limite.')
    print('Diferença de velocidade: {} Km/h'.format(velf))

else:
    print('A velociade do carro está dentro do limite permitido!!')
