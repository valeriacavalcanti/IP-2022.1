nome = input()
salario = float(input())
vendas = float(input())

comissao = vendas * 0.15

salario += comissao
# salario = salario + comissao

print('TOTAL = R$ {:.2f}'.format(salario))
