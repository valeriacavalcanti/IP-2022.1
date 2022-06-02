pessoas = 100
soma = 0

while (pessoas > 0):
    codigo = int(input())
    if (codigo == 1):
        pessoas -= 4
        soma += 6
    elif (codigo == 2):
        pessoas -= 1
        soma += 2
    elif (codigo == 3):
        pessoas -= 40
        soma += 45
    else:
        pessoas -= 12
        soma += 15

print("R$ {:.2f}".format(soma))
