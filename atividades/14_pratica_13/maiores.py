def somar(lista):
    soma = 0
    for i in range(len(lista)):
        soma += lista[i]
    return soma

def maiores(lista):
    temp = []
    media = somar(lista)/len(lista)
    for i in range(len(lista)):
        if (lista[i] > media):
            temp.append(lista[i])
    return temp

