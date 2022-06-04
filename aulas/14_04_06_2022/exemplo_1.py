# Verificar se é letra ou número

st = input()
qtde = 0

for s in st:
    if ((s >= 'A') and (s <= 'Z')) or ((s >= 'a') and (s <= 'z')) or ((s >= '0') and (s <= '9')):
        qtde += 1

print(qtde)
if (len(st) > 0) and (qtde == len(st)):
    print("SIM")
else:
    print("NÃO")
