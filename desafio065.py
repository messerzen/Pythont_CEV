n=0
s=0
c=0
r='S'
ma=0
me=0
while r=='S':
    n=int(input('Digite um número: '))
    c+=1
    s+=n
    if c==1:
        me=ma=n
    else:
        if n>ma:
            ma=n
        if n<me:
            me=n
    r=str(input('Deseja continuar, sim [S] ou não [N] ? : ')).upper().strip()[0]
med=s/c
print('O maior valor digitado foi {}'.format(ma))
print('A média entre os valores é de {}'.format(med))
print('O menor valor digitado foi {}'.format(me))
