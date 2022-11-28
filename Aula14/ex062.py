#Melhore o desafio 061, perguntando para o usuario se ele quer mostrar mais alguns termos.
#O programa encerra quando ele disser que quer mostrar 0 termos.

primeiro_termo = int(input('Digite o primeiro termo de uma PA: '))
razao = int(input('Digite a razão dessa PA: '))

count = 1
count_termos = 0
termo = primeiro_termo
while count <= 10:
    print('{} -> '.format(termo), end='')
    termo = termo + razao
    count += 1
    count_termos += 1
print('PAUSA\n')

count = int(input('Quantos termos você deseja mostrar a mais? '))

if count > 0:
    while count > 0:
        pausa = count
        count = 0
        while count < pausa:
            print('{} -> '.format(termo), end='')
            termo = termo + razao
            count += 1
            count_termos += 1
        print('PAUSA\n')
        count = int(input('Quantos termos você deseja mostrar a mais? '))

print('Progressão finalizada com {} termos mostrados.'.format(count_termos))