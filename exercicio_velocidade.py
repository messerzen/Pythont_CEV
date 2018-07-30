def multa (velocidade,aniversário):
    if aniversário == 'S':
        velocidade=velocidade - 5
    if velocidade <= 60:
        print('Sem multa')
    if velocidade >= 61 and velocidade <=80:
        print('Multa leve')
    else:
        print('Multa pesada')
vel=int(input('Qual a velocidade que voce estava?'))
ani=str(input('Você está de aniversários hoje? [S/N]')).upper().strip()[0]
valor=multa(vel,ani)
