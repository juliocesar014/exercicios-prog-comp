"""
Faça um programa que receba dois números e execute as
operações listadas a seguir, de acordo com a escolha do
usuário;
"""

numero_1 = float(input("Digite o primeiro número: "))
numero_2 = float(input("Digite o segundo número: "))
codigo = int(input("Digite o código da operação desejada: "))

if codigo == 1 or codigo == 2:
    print("O maior número é: ", max(numero_1, numero_2))

elif codigo == 3 or codigo == 4:
    print("O menor número é: ", min(numero_1, numero_2))

else:
    print("Código inválido.")
