s=0
maior=0
menor=0
nomemaisvelho=''
for c in range(1,5):
   nome= str(input('Digite o nome: '))
   idade=int(input('Digite a idade: '))
   sexo=str(input('Digite o sexo: '))
   s+=idade
   if c == 1 and sexo == 'm':
       maior=idade
       nomemaisvelho=nome
   else:
       if idade>maior and sexo == 'm':
           maior=idade
           nomemaisvelho=nome
   if idade < 20 and sexo == 'f':
        menor+=1

m=s/4
print('A média de idade do grupo é{}: '.format(m))
print('O nome do homem mais velho do grupo é: {}'.format(nomemaisvelho))
print('Tem {} mulheres com idade inferior a 20 anos'.format(menor))

