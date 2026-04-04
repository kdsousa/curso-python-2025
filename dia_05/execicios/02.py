"""
Escreva um programa que crie um dicionário com nomes de frutas
como chaves e seus respectivos preços como valores. Solicite
ao usuário o nome de uma fruta e exiba o preço correspondente.
maça R$1.50
banana R$2.75
uva R$1.90
pera R$1.25
laranja R$0.65
limao R$1.25
goiaba R$2.15
abacaxi R$3.20
jaca R$5.80
"""

hortifruti = {'maca':1.50,
              'banana':2.75,
              'uva':1.90,
              'pera':1.25,
              'laranja':0.65,
              'limao':1.25,
              'goiaba':2.15,
              'abacaxi':3.20,
              'jaca':5.80}

fruta = input('Digiete o nome da fruta: ')

if fruta in hortifruti:
    print(hortifruti[fruta])
else:
    print('Não temos esta fruta!')
    