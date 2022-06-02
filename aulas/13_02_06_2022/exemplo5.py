qtde_num = qtde_mai = qtde_min = qtde_esp = 0
st = input("Digita: ")

for s in st:
    if (s >= '0') and (s <= '9'):
        qtde_num += 1
    elif (s >= 'A') and (s <= 'Z'):
        qtde_mai += 1
    elif (s >= 'a') and (s <= 'z'):
        qtde_min += 1
    else:
        qtde_esp += 1

print('Números:', qtde_num) # 5
print('Maiúsculo:', qtde_mai) # 12
print('Minúsculo:', qtde_min) # 4
print('Especiais:', qtde_esp) # 4

# ifpb.IFPB# IFPB4IFPB2022!
