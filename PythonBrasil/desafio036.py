v1=float(input('Digite o valor da casa: '))
s1=float(input('Digite o valor do seu salário: '))
p1=int(input('Digite em quantos anos você quer pagar: '))
mens=v1/(12*p1)
ex=s1*0.3
if mens > ex:
    print('Você não pode pagar esta casa!')
    print(mens)
else:
    print('O valor da prestação é de R${:.2f}'.format(mens))
