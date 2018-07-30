ano=int(input('Digite o ano de nascimento: '))
idade=2018-ano
if idade <= 9:
    print('Idade {}, categoria mirim'.format(idade))
elif idade > 9 and idade <=14:
    print('Idade {}, categoria infantil.'.format(idade))
elif idade >14 and idade <=19:
    print('Idade {}, categoria junior.'.format(idade))
elif idade >19 and idade <=20:
    print('Idade {}, categoria senior.'.format(idade))
else:
    print('Idade {}, categoria master'.format(idade) )
