numero = int(input())
copia = numero
binario = []
octal = []
hexa = []

# binário
while (numero // 2 != 0):
    binario.insert(0, numero % 2)
    numero = numero // 2

binario.insert(0, numero)
#print(binario)

# octal
numero = copia
while (numero // 8 != 0):
    octal.insert(0, numero % 8)
    numero = numero // 8

octal.insert(0, numero)
#print(octal)

# hexa
numero = copia
while (numero // 16 != 0):
    hexa.insert(0, numero % 16)
    numero = numero // 16

hexa.insert(0, numero)
#print(hexa)


for i in range(len(binario)):
    print(binario[i], end="")

print()

for i in range(len(octal)):
    print(octal[i], end="")

print()

for i in range(len(hexa)):
    if (hexa[i] == 10):
        print("A", end="")
    elif (hexa[i] == 11):
        print("B", end="")
    elif (hexa[i] == 12):
        print("C", end="")
    elif (hexa[i] == 13):
        print("D", end="")
    elif (hexa[i] == 14):
        print("E", end="")
    elif (hexa[i] == 15):
        print("F", end="")
    else:
        print(hexa[i], end="")

print()
