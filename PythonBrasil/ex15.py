h1=float(input('Digite quanto você ganha por hora: '))
n1=float(input('Digite quantas horas voce trabalhou: '))
b=h1*n1
ir=0.11*b
si=0.05*b
ins=0.08*b
l=b-(0.11*b)-(0.05*b)-(0.08*b)
print('+ Salário')
print('- IR (11%): R$ {}'.format(ir))
print(('- INSS (8%): R$ {}'.format(ins)))
print(('Sindicato (5%): R$ {}'.format(si)))
print(('Salário bruto: R$ {} \n Salário líquido: R$ {}'.format(b,l)))