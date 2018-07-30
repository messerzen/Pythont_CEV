primeiro=int(input('Digite o primeiro termo da PA: '))
r=int(input('Digite a razão da PA: '))
t=primeiro
c=1
c2=0
t2=10
total = 0
while t2 !=0:
    total = total + t2
    while c <= total:
        print('{} '.format(t),end='')
        c+=1
        t+=r
    print('PAUSA')
    t2=int(input('Quantos termos você quer mostrar a mais: '))
print('O total de termos da PA é {}'.format(total))

