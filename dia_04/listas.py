# %%

# Uma maneira de definir listas
idades = [27, 20, 29, 38, 41, 55]

print(idades)

# %%

keplin = ["Keplin", "Sousa", "Solteiro", 2500.00, True, 35]

print(keplin)

# %%
type(keplin)

# %%
print(keplin[2])
print(keplin[1:4])

# %%
idades = [27, 20, 29, 38, 41, 55]

print(f'Soma idades: {sum(idades)}')
print(f"Média idades: {sum(idades) / len(idades)}")
print(f'Menor idade: {min(idades)}')
print(f'Maior idade: {max(idades)}')

# %%
keplin = ["Keplin Sousa", "Solteiro", True, 35, ["Stefani", 'Ana', 'Alexia']]

print(len(keplin))
print(keplin[4][0])

exs = keplin[4]
primeira_ex = exs[0]

print(primeira_ex)

# %%
keplin[-1][-1]

# %%
keplin[0:4]
