st = input("Digite uma frase: ")
s = input("Digite um símbolo: ")

# procurar o símbolo (s) na string (st)
# exibir a posição onde encontrou a primeira ocorrência
posicao = -1
for i in range(len(st)):
    if (st[i] == s):
        posicao = i
        break

print(posicao)

# hoje o dia esta nublado
# a: 9
