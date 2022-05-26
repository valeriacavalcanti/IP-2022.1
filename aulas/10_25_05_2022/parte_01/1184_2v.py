operacao = input()
matriz = []
soma = 0
qtde = 0

for i in range(12):
    matriz.append([0] * 12)

for i in range(12):
    for j in range(12):
        matriz[i][j] = float(input())

for i in range(12):
    for j in range(12):
        if (j < i):
            soma += matriz[i][j]
            qtde += 1

if (operacao == 'S'):
    print('{:.1f}'.format(soma))
else:
    print('{:.1f}'.format(soma/qtde))
