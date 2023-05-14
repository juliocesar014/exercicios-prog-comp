"""
Um determinado clube de futebol pretende classificar seus
atletas em categorias. Para isso, o clube contratou você
para criar um programa que executasse essa tarefa.
Baseada na tabela de categorias do clube, construa um
programa que solicite a idade de um atleta e imprima sua
categoria;
- De 05 a 10 anos - Infantil;
- De 11 a 15 anos - Juvenil;
- De 16 a 20 anos - Júnior;
- De 21 a 25 anos - Profissional;
"""

idade = int(input("Digite a idade do atleta: "))
if idade >= 5 and idade <= 10:
    categoria = "Infantil"
    print(f"O atleta tem {idade} anos e sua categoria é {categoria}.")
elif idade >= 11 and idade <= 15:
    categoria = "Juvenil"
    print(f"O atleta tem {idade} anos e sua categoria é {categoria}.")
elif idade >= 16 and idade <= 20:
    categoria = "Júnior"
    print(f"O atleta tem {idade} anos e sua categoria é {categoria}.")
elif idade >= 21 and idade <= 25:
    categoria = "Profissional"
    print(f"O atleta tem {idade} anos e sua categoria é {categoria}.")
