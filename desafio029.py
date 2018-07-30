vel=float(input('Digite a velocidade que o carro estava em km/h: '))
mul=7*(vel-80)
if vel <= 80:
    print('Você estava na velocidade permitida!')
else:
    print('Voce estava acima, e a sua multa é de {}'.format(mul))
print('=Vá se foder!=')