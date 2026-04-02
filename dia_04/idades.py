# %%
idade = [17, 32, 56, 87]

print(idade)

# %%
idade.append(32)

print(idade)

# %%
idades = []

while True:
    idade = input("Entre com a idade: ")

    if idade == "":
        break
    
    idades.append(int(idade))

print(idades)

media = sum(idades) / len(idades)
minimo = min(idades)
maximo = max(idades)
qtd = len (idades)

print("média: ", media)
print("minimo: ", minimo)
print("maximo: ", maximo)
print("quantidade ", qtd)
