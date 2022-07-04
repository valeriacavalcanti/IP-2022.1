qtde = 0

nome = input().upper()
while (nome != 'FIM'):
    distintas = []
    for i in range(len(nome)):
        if (nome[i] >= 'A') and (nome[i] <= 'Z') and (nome[i] not in distintas):
            distintas.append(nome[i])
    if (len(distintas) > 10):
        qtde += 1
    nome = input().upper()

print(qtde)
