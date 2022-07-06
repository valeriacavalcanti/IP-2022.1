# QUESTÃO 01

# Tempo da receita tradicional
h, m, s = input().split("Informe o tempo (hora, minuto, segundo): ")
h, m, s = int(h), int(m), int(s)
tempo = h * 3600 + m * 60 + s

# Tempo da receita secreta: Metade do tempo da receita tradicional.
tempo = tempo // 2

# Converte o tempo da receita secreta em: hora, minuto e segundo.
h = tempo // 3600
m = (tempo % 3600) // 60
s = (tempo % 3600) % 60

print(h, m, s)
