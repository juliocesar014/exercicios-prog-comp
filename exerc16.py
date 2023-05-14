"""
Faça um programa que repita as seguintes tarefas, até que
a palavra ‘nao’ seja digitada:
– Leia a distância percorrida por um atleta;
– Leia o tempo que o atleta levou para percorrer a distância;
– Calcule e exiba sua velocidade média:
▪ Velocidade = distancia / tempo;
– Pergunte ao usuário se o mesmo quer continuar a executar o
programa (o usuário responderá ‘sim’ ou ‘nao’);
"""


while True:
    distancia = float(
        input("Digite a distância percorrida pelo atleta (em metros): "))

    tempo = float(input(
        "Digite o tempo que o atleta levou para percorrer a distância (em segundos): "))

    velocidade_media = distancia / tempo

    print("A velocidade média do atleta foi de",
          velocidade_media, "metros por segundo.")

    opcao = input("Deseja continuar? (sim/nao): ")

    if opcao.lower() == "nao":
        break
