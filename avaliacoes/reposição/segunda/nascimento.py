# QUESTÃO 02

soma = 0
d,m,a = input("Nascimento: ").split('/')
d,m,a = int(d), int(m), int(a)

# Verifica se a data é válida. Ou seja, se a data é anterior ou igual a data atual.
if ((a < 2022) or (a == 2022 and m < 7) or (a == 2022 and m == 7 and d <= 4)):
    data_valida = True
else:
    data_valida = False

# Loop enquanto a data for válida
while (data_valida == True):
    # calcula a idade
    idade = 2022 - a
    # verifica se o aniversário já passou no ano atual
    if (m > 7) or ((m == 7) and d > 4):
        idade -= 1 # no ano atual ainda não houve aniversário

    # totaliza a idade
    soma += idade

    # pergunta a próxima data
    d,m,a = input("Nascimento: ").split('/')

    # Verifica se a data é válida. Ou seja, se a data é anterior ou igual a data atual.
    d,m,a = int(d), int(m), int(a)
    if ((a < 2022) or (a == 2022 and m < 7) or (a == 2022 and m == 7 and d <= 4)):
        data_valida = True
    else:
        data_valida = False

print(soma)
