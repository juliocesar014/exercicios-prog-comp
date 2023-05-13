"""Faça um programa que leia três valores inteiros A, B e C e
diga se a soma de A + B é menor que C;
"""

numero_1 = int(input("Digite o primeiro número: "))
numero_2 = int(input("Digite o segundo número: "))
numero_3 = int(input("Digite o terceiro número: "))
soma = numero_1 + numero_2
if soma < numero_3:
    print("A soma de {} + {} é menor que {}".format(numero_1, numero_2, numero_3))
else:
    print("A soma de {} + {} é maior que {}".format(numero_1, numero_2, numero_3))
