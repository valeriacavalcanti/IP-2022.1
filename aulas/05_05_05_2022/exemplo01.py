import random

qtde = 0
qtde_15 = 0
soma = 0
menor = int(input("Menor: "))
maior = int(input("Maior: "))

if (menor > maior):
    menor, maior = maior, menor

sorteio = random.randint(menor,maior)
num = int(input("Número [{},{}]: ".format(menor, maior)))

while ((num != sorteio) and (num >= menor) and (num <= maior)):
    qtde = qtde + 1
    # qtde += 1
    soma = soma + num
    if (num % 15 == 0):
        qtde_15 += 1
    num = int(input("Número [{},{}]: ".format(menor, maior)))

print(sorteio)
print(num)
print(qtde)
print(soma)
if (qtde != 0):
    print(soma/qtde)
else:
    print("erro")
print(qtde_15)

# resultado do jogo
if (num == sorteio):
    print("Ganhou!")
else:
    print("Perdeu ... :-(")
