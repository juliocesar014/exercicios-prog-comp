"""
Faça um programa que calcula e exibe o salário reajustado
de um funcionário. O percentual de aumento encontra-se
na tabela a seguir;
"""

salario = float(input("Digite o salário do funcionário: "))

if salario < 300:
    novo_salario = salario * 1.45
    print(f"Novo salário com aumento de 45%: {novo_salario}")

elif salario >= 300 and salario <= 600:
    novo_salario = salario * 1.25
    print(f"Novo salário com aumento de 25%: {novo_salario}")

elif salario > 600:
    novo_salario = salario * 1.15
    print(f"Novo salário com aumento de 15%: {novo_salario}")
