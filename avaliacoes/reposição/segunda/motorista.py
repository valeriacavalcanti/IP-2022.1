# QUESTÃO 01

tempo = 0

for i in range(4):
    # Duração da "i" viagem
    h,m,s = input('Tempo: ').split(':')
    h,m,s = int(h),int(m),int(s)
    # Totaliza no tempo gasto das 4 viagens, em segundos.
    tempo += (h * 3600 + m* 60 + s)

# Converte o tempo total em: hora, minuto, segundo.
h = tempo // 3600
m = (tempo % 3600) // 60
s = (tempo % 3600) % 60

print('{}:{}:{}'.format(h,m,s))
