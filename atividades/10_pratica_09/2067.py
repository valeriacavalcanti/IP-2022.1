soma = 0
qtde = int(input())
sucos = [0]*qtde
abaixo = 0

for i in range(qtde):
    sucos[i] = int(input())
    soma += sucos[i]

media = soma / qtde

for i in range(qtde):
    if (sucos[i] < media):
        abaixo += 1

print(soma)
print(soma // 1000)
print(abaixo)
