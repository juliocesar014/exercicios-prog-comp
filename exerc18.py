"""▪ Faça um programa que receba vários números positivos
(enquanto o número 0 não for digitado). O mesmo deverá
exibir o maior número digitado
"""


maior_numero = None

while True:
    numero = float(input("Digite um número positivo: "))

    if numero == 0:
        break

    if numero > 0:
        if maior_numero is None or numero > maior_numero:
            maior_numero = numero

if maior_numero is not None:
    print("O maior número digitado foi:", maior_numero)
else:
    print("Nenhum número positivo foi digitado.")
