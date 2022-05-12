num = int(input())

while (num != 0):
    # range(1, num + 1)
    for i in range(1, num): # 1 2 3 4 ... num
        print(i, end=' ')
    print(num)
    num = int(input())
