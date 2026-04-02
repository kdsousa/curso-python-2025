# %%
16 % 4

# %% 
# Quais numeros são divisivais por 4 no intervalo [4-100]?

count = 4
while count <= 100:
    resto = count % 4
    if resto == 0:
        print(count)
    
    count += 1

# %%
# Quais numeros são divisivais por 4 no intervalo [4-100]?

for numero in range(4, 101):
    if numero % 4 == 0:
        print(numero)
