isento_soma = 0
isento_qtde = 0
qtde_faixa4 = 0
maior = -1

for i in range(10):
    valor = float(input())
    if (valor <= 22847.76):
        isento_soma += valor
        isento_qtde += 1
    elif (valor >= 45012.61) and (valor <= 55976.16):
        qtde_faixa4 += 1
    if (valor > maior):
        maior = valor

print(qtde_faixa4)
if (isento_qtde > 0):
    print("{:.2f}".format(isento_soma/isento_qtde))
else:
    print("SEM ISENTO")
print("{:.2f}".format(maior))
