tela = []
for i in range(8):
    tela.append([0] * 4)

for i in range(20):
    linha, coluna = input().split()
    linha, coluna = int(linha), int(coluna)
    tela[linha][coluna] += 1

maior = -1
for i in range(8):
    for j in range(4):
        if (tela[i][j] > maior):
            maior = tela[i][j]

for i in range(8):
    for j in range(4):
        if (tela[i][j] == maior):
            print(i, j)
