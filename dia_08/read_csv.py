# %%
arquivo = "dados.csv"
# Lendo o arquivo
with open(arquivo) as open_file:
    lines = open_file.readlines()

print(lines)

# %%
# Print linha a linha
for l in lines:
    print(l)

# %%
dados = dict()

chaves = lines[0].strip("\n").split(';')

for c in chaves:
    dados[c] = []

dados

# %%
for l in lines[1:]:
    valores = l.strip('\n').split(';')
    for i in range(len(valores)):
        dados[chaves[i]].append(valores[i])

# %%
dados
