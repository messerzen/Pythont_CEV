cm=ch=ci=0
while True:
    idade=int(input('Idade: '))
    if idade >= 18:
        ci+=1
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F]')).strip().upper()[0]
        if sexo == 'M':
            ch+=1
        if sexo == 'F' and idade <=20:
            cm+=1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print(f'{ci} tem mais de 18 anos')
print(f'{ch} homem foram cadastrados')
print(f'{cm} mulheres tem mais de 20 anos')