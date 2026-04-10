# %%

nome_arquivo = "historia.txt"

#Abre o arquivo em formato de leitura
open_file = open(nome_arquivo)

# %%
print(open_file)

# %%
# Lê os dados do arquivo
conteudo = open_file.read()

print(conteudo)

# %%
# Fecha o arquivo
open_file.close()

# %%
# Melhor forma de ler um arquivo
nome_arquivo = "historia.txt"

with open(nome_arquivo) as open_file:
    conteudo = open_file.read()

print(conteudo)

# %%
