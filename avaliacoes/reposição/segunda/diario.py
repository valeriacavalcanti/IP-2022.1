# QUESTÃO 03

nome = []   # armazenar os nomes
nota1 = []  # armazenar as primeiras notas
nota2 = []  # armazenar as segundas notas
soma = 0

for i in range(10):
    n,n1,n2 = input('Nome, nota1, not2: ').split()
    nome.append(n)
    nota1.append(int(n1))
    nota2.append(int(n2))
    # soma a média do "i" estudante
    soma += (nota1[i] + nota2[i]) / 2

# calcula a média do grupo
media = soma / 10

for i in range(10):
    # verifica se a média do "i" estudante é superior ou igual a média do grupo
    if ((nota1[i] + nota2[i]) / 2 >= media):
        print(nome[i], nota1[i], nota2[i], (nota1[i] + nota2[i])/2)
