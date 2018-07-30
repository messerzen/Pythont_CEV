import random
print('=-'*20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-'*20)
n=0
b= random.randint(0,5)
while True:
    n=int(input('Digite um valor: '))
    escolha=str(input('VOCÊ QUER PAR OU ÍMPAR?[P/I]')).upper().strip()
    sum=n+b
    div=sum%2
    if div==0 and escolha == 'P':
        print(f'Você jogou {n} e o computador {b}. Total de {sum} DEU PAR. VOCÊ GANHOU')
    elif div != 0 and escolha =='I':
        print(f'Você jogou {n} e o computador {b}. Total de {sum} DEU ÍMPAR. VOCÊ GANHOU')
    else:
        break
print('-'*40)
print(f'Você jogou {n} e o computador {b}. Total de {sum} DEU PAR')
print('-'*40)
print('VOCÊ PERDEU ')
