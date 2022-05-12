n1, n2, n3 = input().split()
n1, n2, n3 = int(n1), int(n2), int(n3)

if (n1 < n2) and (n1 < n3):
    if (n2 < n3):
        print(n1, n2, n3, sep='\n')
    else:
        print(n1, n3, n2, sep='\n')
else:
    if (n2 < n3):
        if (n1 < n3):
            print(n2, n1, n3, sep='\n')
        else:
            print(n2, n3, n1, sep='\n')
    else:
        if (n1 < n2):
            print(n3, n1, n2, sep='\n')
        else:
            print(n3, n2, n1, sep='\n')

print()
print(n1, n2, n3, sep='\n')
