"""
Faça um programa que lê a resposta de 15 usuários para a
seguinte pergunta: “Você gosta de beterraba? Digite 1 para
SIM e 2 para NÃO”. Após a coleta da resposta de cada
usuário, o algoritmo deverá exibir a quantidade de
respostas para cada opção;
"""


gosta = 0
nao_gosta = 0

for i in range(15):
    resposta = int(
        input("Você gosta de beterraba? Digite 1 para SIM e 2 para NÃO: "))
    if resposta == 1:
        gosta = gosta + 1
        print("SIM")
    elif resposta == 2:
        nao_gosta = nao_gosta + 1
        print("NÃO")
    else:
        print("Resposta inválida!")
    print(f"Quantidade de pessoas que gostam de beterraba: {gosta}")
    print(f"Quantidade de pessoas que não gostam de beterraba: {nao_gosta}")
