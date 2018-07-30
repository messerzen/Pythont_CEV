print('='*2)
print('Gerador de PA')
print('='*2)
t=int(input('Digite o primeiro termo da pa: '))
r=int(input('Digite a razão da pa: '))
t1=t
n=1
while n<=10:
    print('{} -> '.format(t1), end='')
    n+=1
    t1+=r
print('FIM')
