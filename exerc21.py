"""Faça um programa que lê 10 números, calcula e
exibe:
– O triplo de cada número;
– A mensagem “É positivo”, caso o número digitado seja
positivo, ou “É negativo”, caso seja negativo;
"""

for i in range(10):
    num = int(input("Digite um número: "))
    print(f"O triplo do número {num} é {num*3}")
    if num >= 0:
        print("É positivo")
    else:
        print("É negativo")
