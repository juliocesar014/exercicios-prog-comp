"""
Faça um programa que receba dois números e execute as
operações listadas a seguir, de acordo com a escolha do
usuário;
"""

numero_1 = int(input("Digite o primeiro número: "))
numero_2 = int(input("Digite o segundo número: "))
codigo = int(input("Digite o código da operação: "))

if codigo == 1:
    print(
        f"A média da soma de {numero_1} + {numero_2} é:", (numero_1 + numero_2) / 2)

elif codigo == 2:
    print(f"A diferença do maior pelo menor é: ", numero_1 - numero_2)

elif codigo == 3:
    print(f"O produto entre os números é: ", numero_1 * numero_2)

elif codigo == 4:
    print(f"Divisão do primeiro pelo segundo é: ", numero_1 / numero_2)

else:
    print("Código inválido!")
