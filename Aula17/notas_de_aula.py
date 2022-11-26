'''
LISTAS EM PYTHON

lista.append(item) - Adiciona o item na ultima posição da lista

lista.sort() - Ordena a lista de forma crescente, como parametro pode ter (reverse=True)
ordenando assim de forma decrescente. 

lista.insert(posi, item) - Adiciona o item na posição indicada como primeira parte do parametro

lista.pop(posi) - Sem paramentro ele remove o ultimo elemento da lista, com parametro, remove
o elemento da posição informada

lista.remove(item) - Remove o item colocado como parametro, buscando a partir da posição 0,
ou seja, caso tenha dois itens iguais, a função remove só a primeira ocorrencia, caso o 
elemento não exista, ocorre um erro, logo recomenda-se utilizar uma condicional:
"if item in lista", sendo assim ele verifica se o item está na lista


'''
a = [0, 2, 8, 9]
b = a.copy()
b[2] = 3
print(f'Lista A: {a}')
print(f'Lista B: {b}')