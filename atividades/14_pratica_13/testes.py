from ascii import ascii
from binario import binario
from datas import compara
from distintos import distintos
from divisores import divisores
from hexa import hexa
from maior import maior
from maiores import maiores
from mesclar import mesclar
from octal import octal
from par import par
from pares import  pares
from print_vetor import printV
from print_matriz import printM

# ASCII
ascii(65,90)

print('-' * 10)

# Binário
print(binario(15))
print(binario(7))
print(binario(10))

print('-' * 10)

# Datas
print(compara(12,6,2022, 13,6,2022))
print(compara(13,6,2022, 13,6,2022))
print(compara(14,6,2022, 13,6,2022))

print('-' * 10)

# Distintos
print(distintos([1,2,3,4]))
print(distintos([1,2,3,4,1]))

print('-' * 10)

# Divisores
print(divisores(1))  # 1
print(divisores(2))  # 1 2
print(divisores(3))  # 1 3
print(divisores(6))  # 1 2 3 6
print(divisores(10)) # 1 2 5 10

print('-' * 10)

# Hexa
print(hexa(15))
print(hexa(7))
print(hexa(10))

print('-' * 10)

# Maior
print(maior(10, 20))
print(maior(10, 10))
print(maior(20, 10))

print('-' * 10)

# Maiores
print(maiores([10,20,30,40,50,60,70,80,90,100]))

print('-' * 10)

# Mesclar
print(mesclar([1,3,5,7,9],[2,4,6,8,10,12,14]))

print('-' * 10)

# Octal
print(octal(15))
print(octal(7))
print(octal(10))

print('-' * 10)

# Par
for i in range(1,11):
    print(i, par(i))

# Pares
print(pares([1,2,3,4,5,6]))

print('-' * 10)

# Print Vetor
printV([1,2,3,4,5,6])

print('-' * 10)

# Print Matriz
printM([[1,2,3],[4,5,6],[7,8,9]])
