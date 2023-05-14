"""Faça um programa que lê diversos números positivos e escreve
o dobro de cada um. Quando um número negativo for
digitado, o algoritmo deverá parar de ler números.
"""

numero = int(input("Digite um número: "))

while numero >= 0:
    print(numero * 2)
    numero = int(input("Digite um número: "))
