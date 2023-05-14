"""
Faça um programa que receba o preço
de um produto,
calcule e mostre, de
acordo com as
tabelas a seguir, o
novo preço e a
classificação;
"""

preco = float(input("Digite o preço do produto: "))

if preco < 80:
    classificacao = "Barato"
elif preco >= 80 and preco <= 120:
    classificacao = "Normal"
elif preco > 120 and preco <= 200:
    classificacao = "Caro"
elif preco > 200:
    classificacao = "Muito caro"


if preco < 50:
    novo_preco = preco * 1.05
    print(f"Novo preço: {novo_preco} - Classificação: {classificacao}.")

elif preco >= 50 and preco < 100:
    novo_preco = preco * 1.10
    print(f"Novo preço: {novo_preco} - Classificação: {classificacao}.")

elif preco >= 100:
    novo_preco = preco * 1.15
    print(f"Novo preço: {novo_preco} - Classificação: {classificacao}.")
