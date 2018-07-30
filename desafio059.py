n=6
s=0
m=0
while n != 1 and  n != 2 and  n != 1 and n != 3 and  n != 4 and n != 5:
    v1 = int(input('Digite um valor: '))
    v2 = int(input('Digite outro valor: '))

    print('SOMA [1]')
    print('MULTIPLICAR [2]')
    print('MAIOR [3]')
    print('NOVOS NÚMERO [4]')
    print('SAIR DO PROGRAMA [5]')
    n = int(input('Escolha uma opção: '))
    if  n==1:
        s=v1+v2
        print('A soma é {}'.format(s))
    elif n == 2:
        m=v1*v2
        print('A multiplicação é {}'.format(m))
    elif n==3:
        if v1 > v2:
            m=v1
            print ('O maior valor é {}'. format(m))
        elif v1<v2:
            m=v2
            print('O maior valor é {}'.format(m))
    elif n == 4:
        n=9
    elif n == 5:
         print('EXIT')
