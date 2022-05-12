num = int(input("Digite um valor: "))
maior = num

while (num != 16):
    if (num > maior):
        maior = num
    num = int(input("Digite um valor: "))

print(num)
print(maior)

if (maior == 16):
    print('Nenhum valor válido foi digitado')
else:
    print('Maior =', maior)

# 1 2 3 16
# 3 2 1 16
