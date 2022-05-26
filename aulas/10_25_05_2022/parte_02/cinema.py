lugares = []
qtde = 0

for i in range(10):
    lugares.append([False] * 20)

for i in range(100):
    fila, poltrona = input().split()
    fila, poltrona = int(fila), int(poltrona)
    if (lugares[fila][poltrona] == False):
        lugares[fila][poltrona] = True
        qtde += 1

print(qtde)
