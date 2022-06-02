# ler uma string - contem apenas digitos numericos

num = input("Digite um número: ")
qtde = 0

for i in range(len(num)):
    if (ord(num[i]) >= 48) and (ord(num[i]) <= 57):
        qtde += 1

print(qtde, len(num))
