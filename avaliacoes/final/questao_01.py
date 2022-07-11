qtde = 0
nome = input("Informe o nome: ")

for simbolo in nome:
    if (simbolo >= 'A') and (simbolo <= 'Z'):
        qtde += 1

print("Letras maiúsculas =", qtde)
