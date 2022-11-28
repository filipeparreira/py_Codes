#Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato
# Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# - Apenas os 5 primeiros colocados
# - O ultimos 4 colocados da tabela
# - Uma lista com os times em ordem alfabetica
# - Em que posição na tabela está o time chapecoense

colocados = ('Flamengo', 'Palmeiras', 'Atlético Mineiro', 'Grêmio', 'Atletico Paranaense',
'Santos', 'São Paulo', 'Internacional', 'Fluminense', 'Corintians', 'Fortaleza', 'Bahia',
'Ceara', 'Cruzeiro', 'America Mineiro', 'Atletico Goianiense', 'Chapecoense', 'Botafogo',
'Vasco da Gama', 'Red Bull Bragantino')

print('Os cinco primeiros colocados:\n')

for count in range(0, 5):
    print(f'{count + 1}º colocado: {colocados[count]}')

print('Os quatro ultimos colocados:\n')

for count in range(16, len(colocados)):
    print(f'{count + 1}º colocado: {colocados[count]}')

print(f'Colocados em ordem alfabetica: \n')

colocados_ord = sorted(colocados)

for item in colocados_ord:
    print(item)

posi = colocados.count('Chapecoense')

print(f'\n\nO time Chapecoense está na {posi}º posição')