""" Altere o programa anterior para considerar a quantidade de água """

opcao = int(input("""Qual opção deseja:\n
                1 - Água mineral natural R$1,50 \n
                2- Água mineral natural com gás R$2,50\n"""))

if opcao == 1:
    print(" A garrafa de agua desejada é a de Água Mineral Natual.")
    qtd = int(input("Quantas garrafas deseja?\n"))
    print(" O valor a pagar é de R$",(qtd * 1.50))
elif opcao == 2:
    print(" A garrafa de agua desejada é a de Água Mineral com Gás.")
    qtd = int(input("Quantas garrafas deseja?\n"))
    print(" O valor a pagar é de R$",(qtd * 2.50))
else:
    print("Não temos essa opção/garrafa!")
    