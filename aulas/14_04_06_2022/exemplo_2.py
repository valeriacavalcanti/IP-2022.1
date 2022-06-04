qtde = 0
frase = input("Digite uma frase: ")
simbolo = input("Digite um símbolo: ")

# quantas vezes (frequencia) do símbolo na frase
if (len(frase) < 15):
    limite = len(frase)
else:
    limite = 16
for i in range(10,limite):
    if (frase[i] == simbolo):
        qtde += 1

print(qtde)

# hoje o dia esta nublado
# 0123456789ABCDEF
# a
