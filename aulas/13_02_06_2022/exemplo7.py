nomes = []

for i in range(5):
    nomes.append(input("Digite seu nome: "))

#print(nomes)
for i in range(len(nomes)):
    #print(nomes[i])
    for j in range(len(nomes[i])):
        print(nomes[i][j], end=' '*4)
    print()
