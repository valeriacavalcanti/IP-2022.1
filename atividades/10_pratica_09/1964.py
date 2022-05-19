qtde = int(input())
idades = []
dezembro = 0
soma = 0

for i in range(qtde):
    idade, mes = input().split()
    idade = int(idade)
    mes = int(mes)

    idades.append(idade)
    soma += idade
    if (mes == 12):
        dezembro += 1

media = soma / qtde

print(dezembro)
for i in range(len(idades) - 1, -1, -1):
    if (idades[i] > media):
        print(idades[i])
