n1, n2, n3 = input().split()
n1, n2, n3 = int(n1), int(n2), int(n3)

if (n1 < n2) and (n1 < n3):
    if (n2 < n3):
        print('{}\n{}\n{}'.format(n1, n2, n3))
    else:
        print('{}\n{}\n{}'.format(n1, n3, n2))
else:
    if (n2 < n3):
        if (n1 < n3):
            print('{}\n{}\n{}'.format(n2, n1, n3))
        else:
            print('{}\n{}\n{}'.format(n2, n3, n1))
    else:
        if (n1 < n2):
            print('{}\n{}\n{}'.format(n3, n1, n2))
        else:
            print('{}\n{}\n{}'.format(n3, n2, n1))

print('\n{}\n{}\n{}'.format(n1, n2, n3))
