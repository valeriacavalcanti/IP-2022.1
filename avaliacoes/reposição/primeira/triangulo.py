# QUESTÃO 03

# Leitura dos três valores
l1, l2, l3 = input().split()
l1, l2, l3 = int(l1), int(l2), int(l3)

# Verifica se os três valores foram triângulo
if (l1 < l2 + l3) and (l2 < l1 + l3) and (l3 < l1 + l2):
    # Os três lados formam triângulo, agora é verificar qual tipo foi formado.
    if (l1 == l2) and (l1 == l3):
        print("Equilátero") # três lados iguais
    elif (l1 != l2) and (l1 != l3) and (l2 != l3):
        print("escaleno") # três lados diferentes
    else:
        print("isósceles") # dois lados iguais
else:
    print("Não forma triângulo")
