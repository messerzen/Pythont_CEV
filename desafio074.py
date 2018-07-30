import random
ma=0
me=0
cont=0
lista=(random.randint(1,10),random.randint(1,10),random.randint(1,10),random.randint(1,10),random.randint(1,10))
for c in lista:
    print(c, end=' ')
print(f'\nO maior valor sorteado foi {max(lista)}')
print(f'O menor valor sorteado foi {min(lista)}')