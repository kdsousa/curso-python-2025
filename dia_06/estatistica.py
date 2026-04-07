# %%
def soma(a, b):
    return a + b

soma(5, 6)

# %%
def media(a, b):
    return soma(a, b) / 2

media(8, 10)

# %%
a = float(input( "entre com o valor de a: "))
b = float(input( "entre com o valor de b: "))

print(f'Soma: {soma(a, b)}')
print(f'Média: {media(a, b)}')

# %%
# soma com Varios valores com lista
def soma(valores:list):
    return sum(valores)

# média com Varios valores com lista
def media(valores:list):
    return soma(valores) / len(valores)

print(f'Soma: {soma([10,6,8,9,8,7,6,8,9])}')
print(f'Média: {media([10,6,8,9,8,7,6,8,9])}')

# %%
# # soma com Varios valores com *args
def soma(a, b, *args):
    valores = [a, b] + list(args)
    return sum(valores)

# média com Varios valores com *args
def media(a, b, *args):
    return soma(a, b, *args) / (len(args) + 2)

print(f'Soma: {soma(10,6,8,9,8,7,6,8,9)}')
print(f'Média: {media(10,6,8,9,8,7,6,8,9)}')
