"""
▪ Faça um programa que lê a idade de várias pessoas
(enquanto o usuário digitar valores positivos). Em seguida, o
algoritmo deverá apresentar a quantidade de adolescentes
(de 12 a 17 anos);
"""


idade = int(input("Digite a idade: "))
adoloscente = 0

while idade >= 0:
    if idade >= 12 and idade <= 17:
        adoloscente = adoloscente + 1
        print(
            f"Adolescente! No momento foram enviados {adoloscente} adolescentes.")
    idade = int(input("Digite a idade: "))
