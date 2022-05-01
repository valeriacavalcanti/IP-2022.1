verba = float(input("Valor da verba: "))
valor_compra = float(input("Valor da compra: "))

if (verba == valor_compra):
  print("Só pode comprar os chocolates")
elif (verba > valor_compra):
  print("Comprar chocolate e viajar")
  troco = verba - valor_compra
  print("Troco = R$", troco)
else:
  print("Boa viagem!")