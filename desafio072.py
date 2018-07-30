nro=('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove',
    'dez','onze', 'doze','treze', 'quatroze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
n=22
while True:
    while n>=21:
        n=int(input('Digite um número entre 0 e 20:'))
    if n<=20:
        print(f'Você digitou o número {nro[n]}')
        break