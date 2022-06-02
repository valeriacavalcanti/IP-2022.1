# ler uma string - contem apenas digitos numericos

num = input("Digite um número: ")
numeros = '0123456789'
qtde = 0

for i in range(len(num)):
    if (num[i] in numeros):
        qtde += 1

print(qtde, len(num))
