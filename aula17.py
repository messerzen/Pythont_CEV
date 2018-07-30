# Tupla ()
# Lista []
#-----------------------------
#lanche.append('Elemento') adiciona um elemento
#Formas de deletar
#del lanche[3]
#lanche.pop(3)  sem o número ele deleta o último
#lanche.remove('Pizza') só elimina o primeiro valor da lista
#valores.sort() ordena os valores
#valores.sort(reverse=True) ordena de modo inverso
#len(valores) quantidade de elementos _
# b=a b se iguala à a
#b=a[:] b recebe todos os valores de a

# para criar listas pod-se utilizar valores =list(range(4,11))
#-------------------------------
a=[2,3,4,7]
print(a)
b=a[:]
b[2]=8
print(f'Lista A: {a}')
print(f'Lista B: {b}')

