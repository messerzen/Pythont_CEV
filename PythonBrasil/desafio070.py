tot=0
mais100=0
cont = 0
low=0
lowname = ' '
while True:
    nome=str(input('Digite o nome do produto: '))
    preco=float(input('Digite o preço do produto: '))
    cont+=1
    tot+=preco
    if preco >=1000.00:
        mais100+=1
    if cont == 1:
        low = preco
        lowname=nome
    else:
        if preco < low:
            low=preco
            lowname=nome
    resp=' '
    while resp not in 'SN':
        resp=str(input('Você deseja continuar? [S/N]')).upper().strip()[0]
    if resp == 'N':
        break
print(f'O valor total gasto foi de R$ {tot} ')
print(f'{mais100} produtos custam mais de R$ 1.000,00')
print(f'O nome do produto mais barato é {lowname} e custa R$ {low}')
