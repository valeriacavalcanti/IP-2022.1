lista = [10,20,30,40]
num = int(input("Número: "))

# verificar SE existe
existe = False
for i in range(len(lista)):
    if (lista[i] == num):
        existe = True
        break

if (existe == True):
    print('tem')
else:
    print('nao tem')
