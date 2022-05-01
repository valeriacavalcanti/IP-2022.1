n1 = int(input())
n2 = int(input())
n3 = int(input())

ma = (n1 + n2 + n3) / 3
mp = (n1 * 4 + n2 * 6 + n3 * 8) / 18

if (ma > mp):
    print("MA")
elif (ma < mp):
    print("MP")
else:
    print("TANTO FAZ")
