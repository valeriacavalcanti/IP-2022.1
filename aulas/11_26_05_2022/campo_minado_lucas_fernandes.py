import random

campo = []
for i in range(5):
    campo.append([0] * 5)

# imprimir a matriz
for i in range(5):
    print(campo[i])

# inserir bombas
bombas = int(input("Quantidade de bombas: "))
for i in range(bombas):
    campo[random.randint(0,4)][random.randint(0,4)] = -1

print()

# imprimir a matriz com as bombas
for i in range(5):
    print(campo[i])

# verificar adjacentes (atualizas as dicas)
for linha in range(5):
    for coluna in range(5):
        if (campo[linha][coluna] != -1):
            qtde = 0
            for i in range(-1,2):
                for j in range(-1,2):
                    if (linha+i>=0) and (linha+i<5):
                        if (coluna+j>=0) and (coluna+j<5):
                            if (campo[linha+i][coluna+j] == -1):
                                qtde += 1
            campo[linha][coluna] = qtde

print()

# imprimir a matriz com bombas e dicas
for i in range(5):
    print(campo[i])
