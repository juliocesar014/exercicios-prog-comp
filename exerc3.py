"""Faça um programa que lê o número de gols marcados pelo
Sport e o número de gols marcados pelo Náutico. Escrever
o nome do time vencedor. Caso não haja vencedor,
escrever EMPATE;
"""

gol_sport = int(input("Digite o número de gols do Sport: "))
gol_nautico = int(input("Digite o número de gols do Náutico: "))

if gol_sport > gol_nautico:
    print("Sport venceu!")
elif gol_nautico > gol_sport:
    print("Náutico venceu!")
else:
    print("Empate!")
