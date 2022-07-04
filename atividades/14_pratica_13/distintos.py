def distintos(lista):
    outra = []

    for elemento in lista:
        if elemento not in outra:
            outra.append(elemento)
        else:
            return False
    return True
