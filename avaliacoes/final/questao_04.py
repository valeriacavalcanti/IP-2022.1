def valida(linha, coluna):
    return linha >= 0 and linha <= 5 and coluna >= 0 and coluna <= 5


# PROGRAMA PRINCIPAL

qtde = 0

lotes = []
for i in range(6):
    lotes.append([False] * 6)

linha, coluna = input("Localização do Lote: ").split()
linha, coluna = int(linha), int(coluna)
while (valida(linha, coluna) == True):
    if (lotes[linha][coluna] == False):
        lotes[linha][coluna] = True
        qtde += 1
    linha, coluna = input("Localização do Lote: ").split()
    linha, coluna = int(linha), int(coluna)

print("Lotes vendidos com sucesso:", qtde)
