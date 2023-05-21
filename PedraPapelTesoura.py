#passos para construção de um algoritimo
# 1-analise do problema
# um jogo que selecione um numero aleatorio em um lista, 
# segundo o numero escolhido fazer o resultado do jogo 
# contabilizar quantas rodadas ocorreram

#2- passo: especificação dos requisitos
# entrada: um numero
# saida: resultado;

import random

SeusPontos = 0
MaqPontos = 0

while SeusPontos < 3 and MaqPontos < 3:
    print("Selecione uma opção:\n 1 - Pedra\n 2 - Papel\n 3 - Tesoura\nSua Opção: ")
    opc = int(input())


    def sortear_numero(inicio, fim):
        return random.randint(inicio, fim)

    numero_sorteado = sortear_numero(1, 3)
    print(numero_sorteado)

    if numero_sorteado == 1:
        print("A Máquina Jogou: Pedra")
    elif numero_sorteado == 2:
        print("A Máquina Jogou: Papel")
    else:
        print("A Máquina Jogou: Tesoura")

    if numero_sorteado == opc:
        print("Empate!")
        print("\n")
    elif (numero_sorteado == 1 and opc == 2) or (numero_sorteado == 2 and opc == 3) or (numero_sorteado == 3 and opc == 1):
        print("Você Ganhou!")
        SeusPontos += 1
        print("\n")
    else:
        print("Você Perdeu!")
        MaqPontos += 1
        print("\n")

print("Fim do jogo!")
if SeusPontos > MaqPontos:
    print("Você venceu o jogo!")
    print("\n")
    print("Seus Pontos:",SeusPontos)
    print("Pontos da Maquina: ",MaqPontos )

else:
    print("A Máquina venceu o jogo!")
    print("\n")
    print("Seus Pontos:",SeusPontos)
    print("Pontos da Maquinaa ",MaqPontos )
