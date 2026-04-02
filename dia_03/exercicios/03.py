"""
Faça um programa que receba uma quantidade indefinida de 
valores correspondentes a "saldo em conta",
mas quando o usuário apertar "enter" se, digitar valor algum,
o programa para de receber valores, e exibe a soma de todos
os valores digitados anteriormente.
"""
soma = 0

while True:
    saldo = input('Digite o valor: ')
    if saldo == "":
        break
    soma += float(saldo)
    
print(soma)
