valor = int(input())

c_100 = valor // 100
resto = valor % 100

c_50 = resto // 50
resto = resto % 50

c_20 = resto // 20
resto = resto % 20

c_10 = resto // 10
resto = resto % 10

c_5 = resto // 5
resto = resto % 5

c_2 = resto // 2
c_1 = resto % 2

print(valor)
print(c_100, 'nota(s) de R$ 100,00')
print(c_50, 'nota(s) de R$ 50,00')
print(c_20, 'nota(s) de R$ 20,00')
print(c_10, 'nota(s) de R$ 10,00')
print(c_5, 'nota(s) de R$ 5,00')
print(c_2, 'nota(s) de R$ 2,00')
print(c_1, 'nota(s) de R$ 1,00')
