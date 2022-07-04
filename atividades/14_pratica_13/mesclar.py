from maior import maior

def mesclar(lista1,lista2):
    lista = []
    t1 = len(lista1)
    t2 = len(lista2)
    for i in range(maior(t1, t2)):
        if (i < t1):
            lista.append(lista1[i])
        if (i < t2):
            lista.append(lista2[i])
    return lista
