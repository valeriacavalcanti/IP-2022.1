# QUESTÃO 02

# Valor da compra realizada pelo cliente.
valor = float(input("Informe o valor das compras: "))

# Quantidade de cupons daquela compra
qtde = int(valor // 100)
print(qtde, 'cupom(ns) recebido(s).')

# Verifica se ficou algum valor remanescente para complentar o próximo cupom.
if (valor % 100 > 0):
    print('Falta R$', 100 - valor % 100, 'para completar o último cupom.')
else:
    print('Cupons entregues.')
