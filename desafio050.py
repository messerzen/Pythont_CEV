p1=int(input('Digite o primeiro termo da pa: '))
r=int(input('Digite a razão'))
for c in range (1,6+1):
    t = int(input('Digite qual o número: '))
    if t % 2 == 0:
        s=s+t
print('Soma: {}'.format(s))