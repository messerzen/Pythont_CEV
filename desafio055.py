maior = 0
menor = 0
for c in range (1,5+1):
   peso=float(input('Peso da {} pessoa: '.format(c)))
   if c == 1:
      maior = peso
      menor = peso
   else:
      if peso > maior:
         maior = peso
      if peso < menor:
         menor = peso
print('O maior peso lido foi de {}'.format(maior))
print('O menor peso lido foi de {}'.format(menor))
