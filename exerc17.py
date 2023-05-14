"""
Faça um programa que repita as seguintes tarefas, até que o
código 0 seja digitado:
– Leia o código do produto;
– Leia a quantidade adquirida;
– Se o código for 1, escreva ‘Caderno – R$ 12.00’; Se for 2,
escreva ‘Régua – R$ 2.50’; Se for 3, escreva ‘Borracha – R$
0.25’; Se for 4, escreva ‘Mochila – R$ 50.00’;
– Calcule e exiba o total a ser pago (valor * quantidade);
"""

while True:
    codigo = int(input("Digite o código do produto (digite 0 para sair): "))

    if codigo == 0:
        break

    quantidade = int(input("Digite a quantidade adquirida: "))

    if codigo == 1:
        valor_unitario = 12.00
        produto = "Caderno"
    elif codigo == 2:
        valor_unitario = 2.50
        produto = "Régua"
    elif codigo == 3:
        valor_unitario = 0.25
        produto = "Borracha"
    elif codigo == 4:
        valor_unitario = 50.00
        produto = "Mochila"
    else:
        print("Código inválido!")
        continue

    total_pago = valor_unitario * quantidade

    print(produto, "- R$", valor_unitario)
    print("Total a ser pago:", total_pago)
    print()
