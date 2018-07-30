n=0
c=0
s=0
while True:
    n=int(input('Digite um número: '))
    if n==999:
        break
    c+=1
    s+=n
print('O total de número digitados foi {} e a soma entre eles é {}'.format(c,s))