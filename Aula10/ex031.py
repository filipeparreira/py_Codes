#Desenvolva um programa que pergunte a distancia de um viagem em Km.
#Calcule o preço da passagem cobrando R$0.50 por Km para viagens até 200 Km.
#e R$0.45 para viagens mais longas.

dis = float(input('Digite a distancia da viagem (em Km): '))

if dis <= 200:
    preco = dis * 0.5
else:
    preco = dis * 0.45

print('O valor da passagem para {}Km é de: R${:.2f}'.format(dis, preco))
