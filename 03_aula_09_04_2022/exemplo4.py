"""
  idade <= 15: não pode votar
  idade 16 ou 17: voto não obrigatório
  idade 18 e 70: voto obrigatório
  idade 70: voto não obrigatório
"""

idade = int(input("Idade: "))

if (idade <= 15):
  print("não pode votar")
elif (idade == 16) or (idade == 17):
  print("voto não obrigatório")
elif (idade <= 70):
  print("voto obrigatório")
else:
  print("voto não obrigatório")