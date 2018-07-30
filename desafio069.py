c2=c18=cf=cm=0
d='H'
while True:
    sexo=str(input('Digite o sexo: [M/F]')).upper().strip()[0]
    if sexo =='M' or sexo=='F':
        idade=int(input('Digite a idade: '))
        if sexo=='M':
            cm+=1
        if idade >=18:
            c18+=1
        if sexo =='F':
            cf+=1
        if idade <= 20 and sexo=='F':
            c2+=1
        if d!='S':
            d=str(input('Você deseja continuar? [S/N]')).upper().strip()[0]
            if d=='N':
                break
print(f'O número de pessoas com idade acima de 18 anos é {c18}')
print(f'O número de homens cadastrados é de {cm}')
print(f'O número de mulheres acima de 20 anos é {c2}')
