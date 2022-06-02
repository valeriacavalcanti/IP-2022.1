# ler uma string - contem apenas digitos numericos

num = input("Digite um número: ")
qtde = 0

for s in num:
    if (s >= '0') and (s <= '9'):
        qtde += 1

print(qtde, len(num))
