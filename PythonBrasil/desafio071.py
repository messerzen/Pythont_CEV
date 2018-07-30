print('='*20)
print('{:^30}'.format('BCEV'))
print('='*20)
c1=50
c2=20
c3=10
c4=1
r1=r2=r3=r4=0
while True:
    valor=int(input('Que valor você quer sacar? R$'))
    r1=(valor//c1) ##notas de 50
    res1=valor%c1
    if res1 ==0:
        break
    r2=res1//c2  #notas de 20
    res2=res1%c2
    if res2 == 0:
        break
    r3=res2//c3 #notas de 10
    res3=res2%c3
    if res3 == 0:
        break
    r4=res3//c4 #notas de 1
    res4=res3%c4
    if res4 == 0:
        break
print(f'Total de {r1} notas de R$ {c1}')
print(f'Total de {r2} notas de R$ {c2}')
print(f'Total de {r3} notas de R$ {c3}')
print(f'Total de {r4} notas de R$ {c4}')
print('='*20)
print('Volte sempre ao BCEV! Tenha um bom dia.')
