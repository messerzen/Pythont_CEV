aa=2018
me=0
ma=0
for c in range (0,7):
    a=int(input('Digite o ano do seu nascimento: '))
    i=aa-a
    if i < 18:
        me+=1
    else:
        ma+=1
print('{} São menos de idade'.format(me))
print('{} são maiores de idade'. format(ma))
