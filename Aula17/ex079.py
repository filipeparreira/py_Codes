#Crie um programa onde o usuario pode digitar varios valores numericos e 
# cadastre-os em uma lista. Caso o numero já exista lá dentro, ele não
# será adicionado. No final serão exibidos todos os valores unicos digitados em ordem crescente.

valores = list()

while True:
    num = int(input('Digite um valor: '))
    
    if num not in valores: 
        valores.append(num)
        print('Valor adicionado com sucesso!!')
    else:
        print('Valor duplicado, não vou adicionar...')
        
    op = str(input('Quer continuar? (S/N) ')).upper().strip()
    while op != 'S' and op != 'N':
        op = str(input('Opção incorreta!! Digite S ou N: ')).upper().strip()
    
    if op == 'N':
        print('=-'*20)
        print(f'Você digitou os valores: {sorted(valores)}')
        break


