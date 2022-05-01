verba = float(input("Valor da verba: "))
valor_compra = float(input("Valor da compra: "))

# verba é superior ou igual ao valor da compra
# print(verba >= valor_compra)

if (verba >= valor_compra):
  print("ôba!")
  print("Chocolate")
  print("Pode comprar!")
else:
  print("eita")
  print("boa viagem")
  print("pipa vai ser legal")

'''
  Teste 1: verba 1500 - compra 1000 -> chocolate
  Teste 2: verba 1500 - compra 1500 -> chocolate
  Teste 3: verba 1500 - compra 2000 -> pipa
'''