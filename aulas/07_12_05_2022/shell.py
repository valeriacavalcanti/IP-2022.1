Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
num = 10
type(num)
<class 'int'>
num
10
num = 20
num
20
numeros = [0
           ]
numeros = [10]
numeros = [0]
numeros
[0]
type(numeros)
<class 'list'>
len(numeros)
1
numeros
[0]
numeros = [0]*6
numeros
[0, 0, 0, 0, 0, 0]
len(numeros)
6
numeros = [16]*4
numeros
[16, 16, 16, 16]
len(numeros)
4
numeros = [0]*6
numeros
[0, 0, 0, 0, 0, 0]
numeros[2] = 10
numeros
[0, 0, 10, 0, 0, 0]
numeros[5] = 50
numeros
[0, 0, 10, 0, 0, 50]
numeros[0] = 20
numeros
[20, 0, 10, 0, 0, 50]
numeros[4] = 15
numeros
[20, 0, 10, 0, 15, 50]
numeros[1] = -5
numeros
[20, -5, 10, 0, 15, 50]
numeros[3] = 32
numeros
[20, -5, 10, 32, 15, 50]
numeros[0] = 10
numeros
[10, -5, 10, 32, 15, 50]
numeros[8] = 1
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    numeros[8] = 1
IndexError: list assignment index out of range
out of rang
SyntaxError: invalid syntax



numeros = [0,0,0,0]
nuemros
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    nuemros
NameError: name 'nuemros' is not defined. Did you mean: 'numeros'?
numeros
[0, 0, 0, 0]
len(numeros)
4
type(numeros)
<class 'list'>




for i in range(4):
    print(numeros)
    numeros[i] = int(input('número: '))
    print(numeros)
    print()

    
[0, 0, 0, 0]
número: 2
[2, 0, 0, 0]

[2, 0, 0, 0]
número: -17
[2, -17, 0, 0]

[2, -17, 0, 0]
número: 3
[2, -17, 3, 0]

[2, -17, 3, 0]
número: 23
[2, -17, 3, 23]

