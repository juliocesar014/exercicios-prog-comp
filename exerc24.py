"""Cada espectador de um cinema respondeu a um questionário
no qual constava sua opinião em relação ao filme: ótimo – 3,
bom – 2, regular – 1. Faça um programa que receba a opinião
de 5 espectadores, calcule e mostre:
– A quantidade de pessoas que responderam ótimo;
– A quantidade de pessoas que responderam bom;
– A quantidade de pessoas que responderam regular;
"""

otimo = 0
bom = 0
regular = 0

for i in range(15):
    resposta = int(
        input("Você gostou do Filme? Digite 3 para ÓTIMO, 2 para BOM & 1 para REGULAR: "))
    if resposta == 3:
        otimo = otimo + 1
        print("ÓTIMO")
    elif resposta == 2:
        bom = bom + 1
        print("BOM")
    elif resposta == 1:
        regular = regular + 1
        print("REGULAR")
    else:
        print("Resposta inválida!")
    print(f"Quantidade de pessoas que avaliram como ÓTIMO o filme: {otimo}")
    print(f"Quantidade de pessoas que avaliram como BOM o filme: {bom}")
    print(
        f"Quantidade de pessoas que avaliram como REGULAR o filme: {regular}")
