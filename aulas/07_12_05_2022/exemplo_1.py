soma = 0
qtde = 0
numeros = [0] * 6 # [0 0 0 0 0 0]

for i in range(6):
    numeros[i] = int(input('Número {}: '.format(i + 1)))
    soma += numeros[i] # soma = soma + numero

print(numeros) # todos os números digitados
print(soma)
media = soma / 6
print(media)

# quantidade de números com valor acima da média
for i in range(6):
    if (numeros[i] > media):
        qtde += 1 # qtde = qtde + 1

print('quantidade =', qtde)

# exibir os valores
for i in range(6):
    if (numeros[i] > media):
        print(numeros[i])
