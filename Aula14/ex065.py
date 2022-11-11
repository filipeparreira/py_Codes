#Crie um programa que leia varios numeros inteiros pelo teclado. No final da execução,
#mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
#O programa deve perguntar ao usuario se ele quer ou não continuar a digitar os valores.
opcao = 's'
maior = 0
menor = 0
count = 0
soma = 0
while opcao == 's':
    num = int(input('Digite um valor: '))
    soma = soma + num
    count += 1
    if num >= maior:
        maior = num
    else:
        menor = num
    opcao = str(input('Você deseja continuar digitando valores (S/N): ')).lower().strip()

    if opcao != 's' and opcao != 'n':
        while opcao != 's':
            opcao = str(input('Opção inválida digite S ou N: '))

    if opcao == 'n':
        print('A média dos valores é: {:.2f}\nMaior: {}\nMenor: {}'.format(soma/count, maior, menor))
        exit()
    
    
