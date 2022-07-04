bombas = int(input())
campo = []
for i in range(4):
    campo.append([0] * 6)

for i in range(bombas):
    l, c = input().split()
    l, c = int(l) - 1, int(c) - 1
    campo[l][c] = -1

l, c = input().split()
l, c = int(l) - 1, int(c) - 1

if (campo[l][c] == -1):
    print('B')
else:
    dica = 0
    if (l - 1 >= 0) and (campo[l-1][c] == -1):
        dica += 1
    if (l + 1 < 4) and (campo[l+1][c] == -1):
        dica += 1
    if (c - 1 >= 0) and (campo[l][c-1] == -1):
        dica += 1
    if (c + 1 < 6) and (campo[l][c+1] == -1):
        dica += 1
    if (l-1 >= 0) and (c-1 >= 0) and (campo[l-1][c-1] == -1):
        dica += 1
    if (l-1 >= 0) and (c+1 < 6) and (campo[l-1][c+1] == -1):
        dica += 1
    if (l+1 < 4) and (c-1 >= 0) and (campo[l+1][c-1] == -1):
        dica += 1
    if (l+1 < 4) and (c+1 < 6) and (campo[l+1][c+1] == -1):
        dica += 1
    if (dica == 0):
        print("X")
    else:
        print(dica)
