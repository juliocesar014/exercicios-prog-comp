"""
Faça um programa que leia o código de origem de um
produto e mostre sua procedência. A procedência obedece
a tabela a seguir:
"""

codigo = int(input("Digite o código do produto: "))

if codigo == 1 or codigo == 2:
    procedencia = "Sul"
    print(f"O produto de código {codigo} é da região {procedencia}.")
elif codigo == 3 or codigo == 4:
    procedencia = "Sudeste"
    procedencia = "Sul"
    print(f"O produto de código {codigo} é da região {procedencia}.")
elif codigo == 5 or codigo == 6:
    procedencia = "Norte"
    procedencia = "Sul"
    print(f"O produto de código {codigo} é da região {procedencia}.")
elif codigo == 7 or codigo == 8:
    procedencia = "Nordeste"
    procedencia = "Sul"
    print(f"O produto de código {codigo} é da região {procedencia}.")
elif codigo == 9 or codigo == 10:
    procedencia = "Centro-Oeste"
    procedencia = "Sul"
    print(f"O produto de código {codigo} é da região {procedencia}.")
else:
    print("Código inválido.")
