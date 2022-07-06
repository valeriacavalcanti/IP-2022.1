# QUESTÃO 01

# Não é necessário criar essa função. No caso, ela recebe uma string e retorna uma cópia sem acentuação.
def limpar(st):
    temp = ''
    for s in st:
        if (s.isalnum() or s == ' '):
            temp += s
    return temp

# PROGRAMA PRINCIPAL

palavras = []    # palavras encontradas nos prvérbios
qtde = []       # contator da respectiva palavra encontrada

for i in range(4):
    proverbio = input("Proverbio: ").upper()
    # quebra (split) o provérbio (limpo, ou seja, sem acentuação) em palavras.
    for p in limpar(proverbio).split():
        # verifica se a palavra é nova, ou seja, não está na lista de palavras conhecidas
        if (p not in palavras):
            # insere a nova palavra na lista de palavras conhecidas e seu respectivo contador.
            palavras.append(p)
            qtde.append(1)
        else:
            # a palavra já é conhecida, apenas incrementa seu respectivo contador
            qtde[palavras.index(p)] += 1

for i in range(len(palavras)):
    # exibe as palavras conhecidas que possuem contador acima de 1, ou seja,
    # apareceram mais de uma vez, ou seja, é caso de repetição.
    if (qtde[i] > 1):
        print(palavras[i], qtde[i])
