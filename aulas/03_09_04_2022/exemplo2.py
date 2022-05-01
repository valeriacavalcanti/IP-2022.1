verba = float(input("Valor da verba: "))
valor_compra = float(input("Valor da compra: "))

if (verba == valor_compra):
  print("Só pode comprar os chocolates")

if (verba > valor_compra):
    print("Comprar chocolate e viajar")
    troco = verba - valor_compra
    print("Troco = R$", troco)

if (verba < valor_compra):
  print("Boa viagem!")