descricao = [''] * 20
calorias = [0] * 20
soma = 0
maior = -1
mais_800 = 0
acima = 0

for i in range(4):
    descricao[i] = input('Descrição: ')
    calorias[i] = int(input("Calorias: "))
    soma += calorias[i]
    if (calorias[i] > 800):
        mais_800 += 1
    if (calorias[i] > maior):
        maior = calorias[i]

media = soma / 4

print(mais_800, 'alimentos com mais de 800 calorias')

print('Alimento(s) mais calórico(s):')
for i in range(4):
    if (calorias[i] > media):
        acima += 1
    if (calorias[i] == maior):
        print(descricao[i])

print(acima, 'alimentos com valor calórico acima da média.')
