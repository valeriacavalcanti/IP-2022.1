memoria = []

num = int(input())
while (num not in memoria):
    memoria.append(num)
    num = int(input())

for i in range(len(memoria)):
    print(memoria[i])
