# converter para maiusculo
outra = ""
st = input("Digite uma palavra: ")
print(st)

#print(ord('A'), ord('a'), ord('a') - ord('A'))
#print(ord('B'), ord('b'), ord('b') - ord('B'))
#print(ord('Z'), ord('z'), ord('z') - ord('Z'))

for s in st:
    if (s >= 'a') and (s <= 'z'):
        outra += chr(ord(s) - 32)
    else:
        outra += s

print(outra)
