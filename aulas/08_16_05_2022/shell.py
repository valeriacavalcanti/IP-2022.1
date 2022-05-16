Python 3.8.2 (v3.8.2:7b3ab5921f, Feb 24 2020, 17:52:18) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> lista1 = [12]*4
>>> lista1
[12, 12, 12, 12]
>>> len(lista1)
4
>>> lista2 = []
>>> lista2
[]
>>> type(lista2)
<class 'list'>
>>> len(lista2)
0
>>> lista2.append(10)
>>> lista2
[10]
>>> lista2.append(20)
>>> lista2
[10, 20]
>>> lista2.append(30)
>>> lista2
[10, 20, 30]
>>> lista2.insert(0, 40)
>>> lista2
[40, 10, 20, 30]
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> lista = [10,20,30,40]
>>> lsita
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    lsita
NameError: name 'lsita' is not defined
>>> lista
[10, 20, 30, 40]
>>> 
>>> 
>>> 
>>> for i in range(4):
	print(i, lista[i])

	
0 10
1 20
2 30
3 40
>>> for i in range(len(lista), -1, -1):
	print(i)

	
4
3
2
1
0
>>> for i in range(len(lista), -1, -1):
	print(i, lista[i])

	
Traceback (most recent call last):
  File "<pyshell#35>", line 2, in <module>
    print(i, lista[i])
IndexError: list index out of range
>>> for i in range(len(lista)-1, -1, -1):
	print(i, lista[i])

	
3 40
2 30
1 20
0 10
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> qtde = int(input())
10
>>> numeros = input()
1 2 3 4 -5 6 7 8 9 10
>>> numeros
'1 2 3 4 -5 6 7 8 9 10'
>>> type(numeros)
<class 'str'>
>>> numeros = input().split()
1 2 3 4 -5 6 7 8 9 10
>>> numeros
['1', '2', '3', '4', '-5', '6', '7', '8', '9', '10']
>>> type(numeros)
<class 'list'>
>>> numeros = int(numeros)
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    numeros = int(numeros)
TypeError: int() argument must be a string, a bytes-like object or a number, not 'list'
>>> for i in range(qtde):
	numeros[i] = int(numeros[i])

	
>>> numeros
[1, 2, 3, 4, -5, 6, 7, 8, 9, 10]
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> numeros
[1, 2, 3, 4, -5, 6, 7, 8, 9, 10]
>>> 