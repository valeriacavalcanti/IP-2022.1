verba = float(input("Valor da verba: "))
valor_compra = float(input("Valor da compra: "))

if (verba == valor_compra):
  print("Só pode comprar os chocolates")
else:
  # verba é DIFERENTE do valor da compra
  if (verba > valor_compra):
    print("Comprar chocolate e viajar")
    troco = verba - valor_compra
    print("Troco = R$", troco)
  else:
    print("Boa viagem!")


"""
 # Teste 1: 1000 - 800 -> troco
 # Teste 2: 1000 - 1000 -> só chocolate
 # Teste 3: 1000 - 1200 -> viagem!
"""