producao = int(input())
capacidade = int(input())

qtde = producao // capacidade
resto = producao % capacidade

if (resto == 0):
    print("{} 0".format(qtde))
else:
    print("{} {}".format(qtde + 1, capacidade - resto))
