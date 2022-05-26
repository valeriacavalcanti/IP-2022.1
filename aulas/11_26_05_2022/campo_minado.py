campo = []
for i in range(5):
    campo.append([0] * 5)

# imprimir a matriz
for i in range(5):
    print(campo[i])

# inserir bombas
campo[1][0] = -1
campo[0][3] = -1
campo[2][2] = -1
campo[2][4] = -1
campo[4][4] = -1

print()

# imprimir a matriz
for i in range(5):
    print(campo[i])

# atualizar as dicas!
for i in range(5):
    for j in range(5):
        if (campo[i][j] != -1):
            qtde = 0 # contador de bombas adjacentes
            # i-1,j-1
            if (i-1>=0) and (j-1>=0) and (campo[i-1][j-1]==-1):
                qtde += 1
            # i-1,j
            if (i-1>=0) and (campo[i-1][j]==-1):
                qtde += 1
            # i-1,j+1
            if (i-1>=0) and (j+1<5) and (campo[i-1][j+1]==-1):
                qtde += 1
            # i,j-1
            if (j-1>=0) and (campo[i][j-1]==-1):
                qtde += 1
            # i,j+1
            if (j+1<5) and (campo[i][j+1]==-1):
                qtde += 1
            # i+1,j-1
            if (i+1<5) and (j-1>=0) and (campo[i+1][j-1]==-1):
                qtde += 1
            # i+1,j
            if (i+1<5) and (campo[i+1][j]==-1):
                qtde += 1
            # i+1,j+1
            if (i+1<5) and (j+1<5) and (campo[i+1][j+1]==-1):
                qtde += 1
            campo[i][j] = qtde

print()

# imprimir a matriz
for i in range(5):
    print(campo[i])
