n=input('Digite algo: ')
a1=type(n)
a2=n.isspace()
a3=n.isnumeric()
a33=n.isalpha()
a4=n.isalnum()
a5=n.isupper()
a6=n.islower()
a7=n.istitle()


print('O tipo primitivo desse valor é ', a1)
print('Só tem espaços?', a2)
print('É numerico?', a3)
print('É alfabetico?', a33)
print('É alfanumerico?', a4)
print('Está em maiúscula?', a5)
print('Está em minúscula?', a6)
print('Está captalizada?', a7)