#Crie um programa que tenha uma tupla com varias palavras, depois disso, voce deve mostrar
# para cada palavra quais são suas vogais

palavras = ('Banana', 'Pera', 'Jabuticaba')

for palavra in palavras:
    a = palavra.lower().count('a')
    e = palavra.lower().count('e')
    i = palavra.lower().count('i')
    o = palavra.lower().count('o')
    u = palavra.lower().count('u')
    
    if a == 0 and e == 0 and i == 0 and o == 0 and u == 0:
        print(f'A palavra {palavra} não tem vogais.')
    else:
        print(f'A palavra {palavra} tem os seguintes vogais: ', end='')
        if a != 0:
            print('a', end=' ')
        if e != 0:
            print('e', end=' ')
        if i != 0:
            print('i', end=' ')
        if o != 0:
            print('o', end=' ')
        if u != 0:
            print('u', end=' ')
    print('\n')    

        