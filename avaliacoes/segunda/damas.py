qtde = 0
tabuleiro = []
for i in range(8):
    tabuleiro.append([False]*8)

# inserir as pecas vermelhas
for i in range(0,3): # 0 1 2
    if (i % 2 == 0):
        for j in range(1, 8, 2): # 1 3 5 7
            tabuleiro[i][j] = True
    else:
        for j in range(0, 8, 2): # 0 2 4 6
            tabuleiro[i][j] = True

# inserir as pecas amarelas
for i in range(5, 8): # 5 6 7
    if (i % 2 == 1):
        for j in range(0, 8, 2):
            tabuleiro[i][j] = True
    else:
        for j in range(1, 8, 2):
            tabuleiro[i][j] = True

# ler os movimentos
for i in range(20):
    #origem, destino = input().split("-")
    #x1, y1 = origem.split()
    #x2, y2 = destino.split()
    x1, y1, lixo, x2, y2 = input().split()
    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
    if (tabuleiro[x1][y1] == True) and (tabuleiro[x2][y2] == False):
        qtde += 1
        tabuleiro[x1][y1] = False
        tabuleiro[x2][y2] = True

# exibir quantos são válidos
print(qtde)
