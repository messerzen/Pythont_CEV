import random
n1=input('Digite um nome: ')
n2=input('Digite um outro nome: ')
n3=input('Digite outro nome: ')
n4=input('Digite um nome: ')
lista = [n1,n2,n3,n4]
es=random.choice(lista)
print('O aluno sorteado foi: {}'.format(es))
