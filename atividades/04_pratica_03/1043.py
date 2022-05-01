n1, n2, n3 = input().split()
n1, n2, n3 = float(n1), float(n2), float(n3)

if (n1 + n2 > n3) and (n1 + n3 > n2) and (n2 + n3 > n1):
  perimetro = n1 + n2 + n3
  print('Perimetro = {:.1f}'.format(perimetro))
else:
  area = ((n1 + n2) * n3 ) / 2
  print('Area = {:.1f}'.format(area))
