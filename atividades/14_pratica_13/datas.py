def compara(d1,m1,a1,d2,m2,a2):
    if (a1 < a2):
        return -1
    elif (a1 > a2):
        return 1
    elif (m1 < m2):
        return -1
    elif (m1 > m2):
        return 1
    elif (d1 < d2):
        return -1
    elif (d1 > d2):
        return 1
    else:
        return 0
