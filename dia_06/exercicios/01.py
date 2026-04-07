"""
Faça um programa que receba um número.
Verifique se o número informado é par ou ímpar.
Exiba o resultado da seguinte maneira:
    O número x é impar
ou
    O número x é par
"""
# %%

def par_impar(numero:int):
    if numero % 2 == 0:
        print(f'O número {numero} é Par')
    elif numero % 2 == 1:
        print(f'O número {numero} é Impar')
    else:
        print(f'O que digitou não é um numero!')
    
# %%
par_impar(9)
par_impar(12)
par_impar(2658)
par_impar(8)
par_impar(2.89)

numero = input('Entre com um número: ')
numero = int(numero)

par_impar(numero)
