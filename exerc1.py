"""
Faça um programa que receba três notas de um aluno, calcule sua média final e diga se o mesmo está aprovado ou reprovado. 
(Se sua média for maior ou igual a 5, o aluno está aprovado, se for menor, está reprovado).
"""

nota1 = int(input("Digite a primeira nota: "))
nota2 = int(input("Digite a segunda nota: "))
nota3 = int(input("Digite a terceira nota: "))
media = (nota1 + nota2 + nota3) / 3
if media >= 5:
    print(f"Aluno aprovado! Com média: {media}")
