qtde = int(input())

codigos = [0] * qtde
nomes = [''] * qtde
votos = [0] * qtde

votantes = 0

# cadastro das candidatas
for i in range(qtde):
    codigos[i], nomes[i] = input().split()
    codigos[i] = int(codigos[i])

# ler os votos
voto = int(input())
while (voto != 0):
    votantes += 1
    # registrar o voto na candidata
    for i in range(qtde):
        if (codigos[i] == voto):
            votos[i] += 1
            break
    voto = int(input())

print(votantes)
for i in range(qtde):
    print(codigos[i], nomes[i], votos[i])
