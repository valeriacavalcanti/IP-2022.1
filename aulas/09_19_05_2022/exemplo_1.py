matriz = []

for i in range(6):
    matriz.append([0] * 3)

print(matriz)
#matriz[2][0] = 80
#matriz[2][1] = 80
#matriz[2][2] = 80
#for i in range(len(matriz[2])):
#    matriz[2][i] = 80

for i in range(6):
    for j in range(3):
        matriz[i][j] = 100 # int(input())

print(matriz)

for i in range(6):
    for j in range(3):
        print(i, j, matriz[i][j])

