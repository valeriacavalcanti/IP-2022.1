def frete (valor):
    if valor <= 100:
        return valor * 0.1
    elif valor <= 200:
        return valor * 0.08
    else:
        return valor * 0.06


def vencido(dia, mes, ano):
    if ano < 2022:
        return True
    elif ano > 2022:
        return False
    elif mes < 6:
        return True
    elif mes > 6:
        return False
    elif dia < 27:
        return True
    else:
        return False


def decimal(binario):
    soma = 0
    tam = len(binario)
    for i in range(len(binario)):
        soma += int(binario[i]) * 2 ** (tam - i - 1)
    return soma

def remover(st):
    nova = ''
    for s in st:
        if s.upper() not in 'AEIOU':
            nova += s
    return nova

def remover2(st):
    for s in 'aeiouAEIOU':
        st = st.replace(s, '')
    return st
