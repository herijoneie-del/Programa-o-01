m1 = {'id':1,'nome':"'tou bom"} 
m2 = {'id':2,'nome':"por enquanto"}

print(f'\n{m1}\n{m2}')

print(f'Nome:{m1["nome"]}')
print(f'ID:{m1["id"]}')
print(f'Nome:{m1["nome"]}')

print(m1.keys())
print(m1.values())

m1['estilo']='Pop portuguesa'
m2['estilo']='Rap Tuga'
musicas = []

musicas.append(m1)
musicas.append(m2)

print(musicas)
for musica in musicas: 
    print(musicas)
    print(f'ID:{musica["id"]}')
    print(f'Nome:{musica["nome"]}')

musicas.append({'id':3,'nome':'Welcome to the pleasure'})
musicas[2]['estilo']='Rap tuga'
for musica in musicas:
    print(f'ID:{musica["id"]}')
    print(f'Nome:{musica["nome"]}')
    print('estilo')

for musica in musicas:
    if musica['estilo'] == 'Rap tuga':
        for chave,valor in musica.items():
            print(f'{chave}:{valor}')



