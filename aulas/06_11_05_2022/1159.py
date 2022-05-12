num = int(input())
while (num != 0):
    if (num % 2 == 1):
        num = num + 1
    soma = 0
    for i in range(5):
        soma = soma + num
        num = num + 2
    print(soma)
    num = int(input())
