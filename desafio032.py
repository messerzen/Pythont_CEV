ano=int(input('Digite o ano: '))
div=ano%400
if div==0:
    print('O ano {} é bissexto!'.format(ano))
else:
    print('O ano não bissexto!')
print('==========')
