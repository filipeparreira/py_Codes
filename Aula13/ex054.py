#Crie um programa que leia o ano de nascimento de sete pessoas. No final mostre quantas
#pessoas não atinjiram a maioridade e quantas pessoas já são de maior



from datetime import date 
data_atual = date.today()

de_maior = 0
de_menor = 0

for count in range(0, 7):
    ano = int(input('Digite o ano de nascimento da pessoa {}: '.format(count + 1)))
    if (data_atual.year - ano) >= 21:
        de_maior += 1
    else:
        de_menor += 1

print('Quantidade de pessoas com mais de 18 anos: ', de_maior)
print('Quantidade de pessoas com menos de 18 anos: ', de_menor)
