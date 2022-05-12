nomes = [''] * 6
numeros = [0] * 6

for i in range(6):
    print('Pessoa: ', i + 1)
    nomes[i] = input("Nome: ")
    numeros[i] = int(input('Número: '))

#print(nomes)
#print(numeros)

for i in range(6):
    print(i + 1, nomes[i], numeros[i])
