binario = []
soma = 0

num = int(input())
while (num == 0 or num == 1):
    binario.append(num)
    num = int(input())

#print(binario)
tamanho = len(binario)
for i in range(tamanho):
    soma += binario[i] * 2 ** (tamanho - i - 1)

print(soma)
