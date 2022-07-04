matriz = []

for i in range(4):
    matriz.append([-1] * 6)

qtde_bombas = int(input())

#Alocando as bombas na matriz
for i in range(qtde_bombas):
    linha, coluna = input().split()
    linha, coluna = int(linha) - 1, int(coluna) - 1

    matriz[linha][coluna] = 'B'

#Recebendo linha e coluna da jogada
linha, coluna = input().split()
linha, coluna = int(linha) - 1, int(coluna) - 1

count_bombas = 0

#Algoritmo para identificar a quantidade de bombas ao redor de uma célula
for i in range(-1, 2):
    for j in range(-1, 2):
        if (linha + i >= 0 and linha + i <= 3) and (coluna + j >= 0 and coluna + j <= 5):
            if matriz[linha + i][coluna + j] == 'B':
                count_bombas += 1

if matriz[linha][coluna] == 'B':
    print('B')
elif count_bombas == 0:
    print('X')
elif count_bombas != 0:
    print(count_bombas)
