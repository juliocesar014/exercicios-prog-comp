"""
Faça um programa que calcula e exibe o salário reajustado
de um funcionário. O percentual de aumento encontra-se
na tabela a seguir;
"""

salario = float(input("Digite o salário: "))

if salario <= 300:
    print(f"Seu salário sem comissão foi: R$ {salario}" + "\n" +
          f"Seu salário reajustado é: R$ {salario + (salario * 0.35)}")

elif salario > 300:
    print(f"Seu salário sem comissão foi: R$ {salario}" + "\n" +
          f"Seu salário reajustado é: R$ {salario + (salario * 0.15)}")
