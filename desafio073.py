times = ('Flamengo', 'São Paulo', 'Atlético-MG', 'Grêmio', 'Internacional', 'Cruzeiro',
         'Palmeiras', 'Corinthians', 'Fluminense', 'Botafogo', 'Vasco', 'Sport', 'Vitória', 'América-MG',
         'Santos', 'Bahia', 'Chapecoense', 'Paraná Clube', 'Atlético-PR', 'Ceará')

print(f'Os cinco primeiros colodados são {times[:5]}')
print(f'Os últimos quatro colodados são {times[-4:]}')
print(sorted(times))
print(f'A posição da chapecoense é {times.index("Chapecoense")+1}')