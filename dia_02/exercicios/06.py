""" Faça um programa que vende um garrafa de agua
        - Se o cliente escolher agua mineral natural, será cobrado R$1,50
        - Se o cliente escolher água mineral com gás, será cobrado R$2,50
"""
opcao = int(input("""Qual opção deseja:\n
                1 - Água mineral natural R$1,50 \n
                2- Água mineral natural com gás R$2,50\n"""))

if opcao == 1:
    print(" A garrafa de agua desejada é a de Água Mineral Natual.")
    print(" O valor a pagar é de R$1,50")
elif opcao == 2:
    print(" A garrafa de agua desejada é a de Água Mineral com Gás.")
    print(" O valor a pagar é de R$2,50")
else:
    print("Não temos essa opção/garrafa!")
