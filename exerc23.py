"""Faça um programa que recebe o preço de 10 produtos e
exibe o valor do produto mais caro;
"""

maior_preco = None

for i in range(10):
    preco = float(input("Digite o preço do produto {}: ".format(i)))

    if maior_preco is None or preco > maior_preco:
        maior_preco = preco

if maior_preco is not None:
    print("O produto mais caro custa:", maior_preco)
