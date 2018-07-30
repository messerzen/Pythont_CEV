n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
if n1 < n2:
    print('{} é maior'.format(n2))
elif n1 > n2:
    print('{} é o maior.'.format(n1))
else:
    print('Não existe valor maior, os dois são iguais.')
