"""
  até 400: 2 vezes
  > 400 e < 800: 4 vezes
  > 800 e < 1200: 6 vezes
  > 1200 e < 2000: 8 vezes
  > 2000: 10 vezes
"""

valor = float(input("Valor da compra: "))

if (valor <= 400):
  parcelas = 2
elif (valor <= 800):
  parcelas = 4
elif (valor <= 1200):
  parcelas = 6
elif (valor <= 2000):
  parcelas = 8
else:
  parcelas = 10

print(parcelas, "parcelas de R$", valor/parcelas)