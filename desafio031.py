d=float(input('Digite a distância da viagem em km: '))
if d <= 200:
    p=0.5*d
    print('O custo da viagem é {:.2f}'.format(p))
else:
    p=0.45*d
    print('O custo da viagem é {:.2f}'.format(p))
print('=fim do programa=')