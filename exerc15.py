"""Faça um programa que lê a idade de várias pessoas, até que
uma idade negativa seja digitada. O algoritmo deverá
calcular e exibir a quantidade de pessoas, de acordo com as
faixas etárias apresentadas na tabela abaixo:
"""

idade = int(input("Digite a idade: "))

while idade >= 0:
    if idade <= 15:
        print("1° Faixa Etária")
    elif idade > 15:
        print("2° Faixa Etária")
    idade = int(input("Digite a idade: "))
