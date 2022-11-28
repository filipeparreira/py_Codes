#Crie um algoritmo que leia um numero e mostre seu dobro, triplo e raiz quadrada

num = int(input('Digite um numero:'))
dob = num * 2
tri = num * 3
r = num ** (1/2)

print('O dobro de {} é {}.\nO triplo de {} é {}\nA raiz quadrada de {} é {:.2f}'.format(num, dob, num, tri, num, r))


