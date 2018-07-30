#map e lambda
def quadrado(var):
    return var**2
lista=[1,2,3,4]
a=list(map(quadrado,lista))
print(a)