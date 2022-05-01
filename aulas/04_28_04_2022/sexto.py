"""
    Ler 10 números e somar.
    Contar os números negativos.
    Somando os números negativos.
"""

"""
  in: 10 20 30 40 50 60
  out: 210
"""

soma = 0
qtde_negativos = 0
soma_negativos = 0

for i in range(6): # 0 1 2 3 4 5
    numero = int(input("Número {}: ".format(i + 1)))
    #print("Soma anterior:", soma)
    soma = soma + numero
    #print("Soma atual:", soma)
    if (numero < 0):
        qtde_negativos = qtde_negativos + 1
        soma_negativos = soma_negativos + numero

print(i)
print(numero)
print(soma)
print(qtde_negativos)
print(soma_negativos)
