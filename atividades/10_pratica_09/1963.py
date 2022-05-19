numero = int(input())
copia = numero
binario = []
octal = []

while (numero // 2 != 0):
    binario.insert(0, numero % 2)
    numero = numero // 2

binario.insert(0, numero)
print(binario)

numero = copia
while (numero // 8 != 0):
    octal.insert(0, numero % 8)
    numero = numero // 8

octal.insert(0, numero)
print(octal)
