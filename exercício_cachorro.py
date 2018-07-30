def contacachorro(st):
    count=0
    for word in st.lower().split():
        if word == 'cachorro':
            count+=1
    return count
total=contacachorro('Esse Cachorro é mais rápido que o outro cachorro')
print(total)