from par import par

def pares(lista):
    qtde = 0
    for i in range(len(lista)):
        if (par(lista[i]) == True):
            qtde += 1
    return qtde
