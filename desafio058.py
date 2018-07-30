import random
n=20
t=0
while n != random.randint (1,10) :
    n=int(input('Digite um número de 1 a 10: '))
    t+=1
print('Você acertou, o número é {} e precisou de {} tentativas.'.format(n,t))