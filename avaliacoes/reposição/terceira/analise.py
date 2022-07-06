# QUESTÃO 02

# Função para verificar se uma data é válida.
def valida(d,m,a):
    if (a < 2022):
        return True
    elif (a == 2022) and (m < 7):
        return True
    elif (a == 2022) and (m == 7) and (d <= 4):
        return True
    else:
        return False

# Função para calcular a idade de uma pessoa
def idade(d, m, a):
    valor = 2022 - a
    # verifica se o aniversário já passou no ano corrente (2022)
    if (m > 7) or ((m == 7) and (d > 4)):
        valor -= 1
    return valor


# PROGRAMA PRINCIPAL

soma = 0

for i in range(8):
    d, m,a = input("Data de nascimento: ").split()
    d,m, a = int(d), int(m), int(a)
    # verifica se a data é válida
    if (valida(d, m, a)):
        # soma a idade
        soma += idade(d,m, a)

print(soma)
