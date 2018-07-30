n=int(input('Digite um número: '))
for c in range (1, n+1):
    if n % c == 0:
        print('\033[39m',end=' ')
    else:
        print('\033[31m',end=' ')
    print('{}'.format(c),end=' ')
