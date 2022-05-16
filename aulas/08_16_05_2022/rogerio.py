num = input()

if (len(num) == 0):
    print('digitou nada')
elif (not num.isdigit()):
    print('nao é numero')
else:
    print('OK')
