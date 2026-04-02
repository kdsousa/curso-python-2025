"""
Faça um programa que receba 4 alturas usando 
um laço de repetição e realize a soma dessas alturas.
"""

soma = 0 # valor final
qtd_entradas = 4 # contador de entradas

while qtd_entradas > 0:
    altura = input("Entre com a altura: ")
    altura = float(altura)
    soma += altura
    qtd_entradas -= 1

print(f"Soma das alturas: {soma}")

# %%
soma = 0 
qtd_entradas = 4

for i in range(qtd_entradas):
    altura = input("Entre com a altura: ")
    altura = float(altura)
    soma += altura

print("Soma das alturas: ", soma)
