import math
n=float(input('Digite o comprimento do cateto oposto:'))
n1=float(input('Digite o comprimento do cateto adjacente: '))
hip=math.hypot(n,n1)
print('A hipotenusa é {}'.format(hip))