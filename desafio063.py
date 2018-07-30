print('='*20)
print('SEQUÊNCIA DE FIBONACCI')
print('='*20)
n=int(input('Digite um valor: '))
f1=0
f2=1
fn=0
c=1
while c<=n:
    print('{} → '.format(fn),end=' ')
    c+=1
    fn=f1+f2
    f2=f1
    f1=fn

