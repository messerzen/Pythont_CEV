palavras=('Guerra', 'Terra', 'Mar', 'Orelha', 'Cavalo', 'Meuzovo')
for vog in palavras:
    print(f'\nNa palavra {vog.upper()} temos', end=' ')
    for letra in vog:
        if letra.lower() in 'aeiou':
            print(letra.lower(), end=' ')

