#Refaça o desafio 051, lendo o primeiro termo e a razão de uma PA,
#mostrando os 10 primeiros termos da progressão usando uma estrutura while.

primeiro_termo = int(input('Digite o primeiro termo de uma PA: '))
razao = int(input('Digite a razão dessa PA: '))

count = 1
termo = primeiro_termo
print('{}º termo: {}'.format(count,  primeiro_termo))

while count < 10:
    count += 1
    termo = termo + razao
    print('{}º termo: {}'.format(count, termo))
