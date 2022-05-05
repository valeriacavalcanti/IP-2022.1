soma = 0
n1 = int(input())
n2 = int(input())

if (n1 > n2):
  n1, n2 = n2, n1

if (n1 % 2 == 1):
  n1 += 2
else:
  n1 += 1

for i in range(n1, n2, 2):
  soma += i

print(soma)
