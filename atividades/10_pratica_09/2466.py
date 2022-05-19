lista = [0] * 6

for i in range(6):
    lista[i] = int(input())

for i in range(5, -1, -1): # 5 4 3 2 1 0
    print(lista[i])
