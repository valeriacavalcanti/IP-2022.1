h, m, s = input("Trecho 1: ").split(":")
h, m, s = int(h), int(m), int(s)
trecho1 = h * 3600 + m * 60 + s

h, m, s = input('Conexão: ').split(":")
h, m, s = int(h), int(m), int(s)
conexao = h * 3600 + m * 60 + s

h, m, s = input("Trecho 2: ").split(":")
h, m, s = int(h), int(m), int(s)
trecho2 = h * 3600 + m * 60 + s

total = trecho1 + conexao + trecho2

h = total // 3600
m = (total % 3600) // 60
s = (total % 3600) % 60

print('Tempo total: {}:{}:{}'.format(h, m, s))
if (trecho1 < trecho2):
    print('Trecho 1 é mais rápido.')
elif (trecho1 > trecho2):
    print('Trecho 2 é mais rápido.')
else:
    print('Os trechos são iguais.')
