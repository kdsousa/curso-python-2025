# %%
lista = [ 2, 132, "banana", ['corola, cerlta, corsa'], True]

lista[2]

# %%
# Dicionaros são pares de chave/valor

dados_pessoa = {'nome':'Kepler',
                'sobrenome': 'Jhonas',
                'filhos': True,
                'formacao':['estatistica', 'bigdata datascience'],
                'cargos':[
                    {'nome': 'ds jr.', 'empresa':'tapps'},
                    {'nome': 'ds pl.', 'empresa':'sas'},
                    {'nome': 'ds sr.', 'empresa':'oracle'},
                    {'nome': 'ds espec.', 'empresa':'tesla'},
                ]}

print(dados_pessoa)

# %%
dados_pessoa['nome']
dados_pessoa['formacao']
dados_pessoa['formacao'][-1]

# %%
print(dados_pessoa['cargos'][-1]['empresa'])

# %%
print(dados_pessoa)
print(dados_pessoa['cargos'])
print(dados_pessoa['cargos'][1]['empresa'])

# %%
dados_pessoa['estado civil'] = 'casado'

print(dados_pessoa)

# %%
dados_pessoa.keys()

# %%
dados_pessoa.values()

# %%
print("itens: ", dados_pessoa.items())

# %%
for i in dados_pessoa:
    print(i, dados_pessoa[i])

# %%
for item in dados_pessoa.items():
    print(item)
