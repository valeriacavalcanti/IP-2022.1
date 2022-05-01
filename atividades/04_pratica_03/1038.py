codigo, qtde = input().split()
codigo, qtde = int(codigo), int(qtde)

if (codigo == 1):
    total = 4 * qtde
elif (codigo == 2):
    total = 4.5 * qtde
elif (codigo == 3):
    total = 5 * qtde
elif (codigo == 4):
    total = 2 * qtde
else:
    total = 1.5 * qtde

print("Total: R$ {:.2f}".format(total))
