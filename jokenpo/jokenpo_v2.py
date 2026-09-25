import random
import time

def menu():
    print("="*30)
    print("JOGO: PEDRA, PAPEL E TESOURA")
    print("="*30)

opcoes= ['pedra', 'papel', 'tesoura']
jogar= True

while jogar:
        
    player_placar=0
    computador_placar=0

    def placar():
            print(f"Você {player_placar}X{computador_placar} Computador")

    while True:
        menu()

        escolha_jogador= input("Escolha uma opção (pedra, papel ou tesoura): ").lower()
        escolha_computador= random.choice(opcoes)

        if escolha_jogador not in opcoes:
            print(f"Escolha inválida! por favor escolha uma das opções: {opcoes}")
            continue
        else:
            print("O computador está pensando...")
            time.sleep(1.3)

        print(f"Você escolheu {escolha_jogador.upper()}")
        print(f"O computador escolheu {escolha_computador.upper()}")

        if escolha_jogador == escolha_computador:
            print("EMPATE!")
            placar()
        elif (escolha_jogador == "pedra" and escolha_computador == "tesoura") or\
            (escolha_jogador == "papel" and escolha_computador == "pedra") or\
            (escolha_jogador == "tesoura" and escolha_computador == "papel"):
            print("VITÓRIA!")
            player_placar = player_placar+1
            placar()
        else:
            print("PERDEU!")
            computador_placar = computador_placar+1
            placar()

        if player_placar == 3 or computador_placar == 3:
            break

    while True:
        print("-"*30)
        print("FIM DE JOGO")
        
        if player_placar == 3:
            print("Você venceu, parabéns!\n")
            break
        else:
            print("O Computador venceu!\n")
            break
    
    escolhas=["s", "n"]
    escolher= input("Deseja continuar o jogo? S ou N. ").lower()
    
    if escolher not in escolhas:
        print("Escolha inválida! Escolha entre S ou N.")
        continue
    elif escolher == "s":
        print("Reiniciando...")
    else:
        jogar = False