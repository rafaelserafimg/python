import random
import time


def menu():
    print("=" * 42)
    print("|" + " " * 40 + "|")
    print("|✊ 📄 ✂️  PEDRA, PAPEL E TESOURA ✂️  📄 ✊|")
    print("|" + " " * 40 + "|")
    print("=" * 42)
    print("|" + " " * 40 + "|")
    print("|" + " " * 11 + "🎮 MENU PRINCIPAL" + " " * 12 + "|")
    print("|" + " " * 40 + "|")
    print("|" + " " * 11 + "🕹️  [1] Jogar" + " " * 17 + "|")
    print("|" + " " * 11 + "📜 [2] Histórico" + " " * 13 + "|")
    print("|" + " " * 11 + "❓ [3] Como jogar" + " " * 12 + "|")
    print("|" + " " * 11 + "🚪 [4] Sair" + " " * 18 + "|")
    print("|" + " " * 40 + "|")
    print("=" * 42)


def placar():
    print(f"🎮 Você {player_placar}X{computador_placar} Computador 🤖")

historico=[]

opcoes = ["pedra", "papel", "tesoura"]
opcoes_menu = [1, 2, 3, 4, ]
opcoes_finais=[1, 2, 3]

player_placar = 0
computador_placar = 0
partidas_jogadas = 0

jogar = True

while jogar:

    menu()

    escolha_menu = int(input("\nEscolha uma das opções acima: "))

    if escolha_menu not in opcoes_menu:
        print(f"Escolha inválida! Escolha uma das opções: {opcoes_menu}")
        continue

    if escolha_menu == 1:
        partidas_jogadas = 0

        escolha_numero_partidas = int(
            input("Quantas partidas queres jogar? ")
        )

        while partidas_jogadas < escolha_numero_partidas:

            escolha_jogador = input(
                "\nEscolha uma opção (pedra, papel ou tesoura): "
            ).lower()

            if escolha_jogador not in opcoes:
                print(
                    f"Escolha inválida! Escolha uma das opções: {opcoes}"
                )
                continue

            escolha_computador = random.choice(opcoes)

            print("O computador está pensando... 🤖")
            time.sleep(1.3)

            print(f"Você escolheu {escolha_jogador.upper()}")
            print(f"O computador escolheu {escolha_computador.upper()}")

            if escolha_jogador == escolha_computador:
                print("EMPATE! 🤝")

            elif (
                escolha_jogador == "pedra"
                and escolha_computador == "tesoura"
            ) or (
                escolha_jogador == "papel"
                and escolha_computador == "pedra"
            ) or (
                escolha_jogador == "tesoura"
                and escolha_computador == "papel"
            ):
                print("VITÓRIA! 🏆")
                player_placar += 1

            else:
                print("PERDEU! 💔")
                computador_placar += 1

            partidas_jogadas += 1

            placar()

        print("-" * 30)
        print("\nFIM DE JOGO\n")

        if player_placar > computador_placar:
            print("🎉 Você venceu, parabéns! 🎉")
            historico.append("VITÓRIA")

        elif computador_placar > player_placar:
            print("❌ O computador venceu! ❌")
            historico.append("DERROTA")
        else:
            print("🤝 Vocês empataram!")
            historico.append("EMPATE")

        escolha_final= int(input("\nOque deseja fazer. [1]Continuar [2]Reiniciar [3]Sair: "))
        if escolha_final not in opcoes_finais:
                print(f"\nEscolha inválida! Escolha uma das opções: [1]Continuar [2]Reiniciar [3]Sair")
                continue
        elif escolha_final == 3:
            break
        elif escolha_final == 2:
            player_placar = 0
            computador_placar = 0
            partidas_jogadas = 0
        else:
            partidas_jogadas = 0
            continue
         

    elif escolha_menu == 2:
        print("\n📜 Histórico...\n")
        if historico == []:
            print("Nenhuma partida jogada ainda.\n")
        else:
            print(historico)

    elif escolha_menu == 3:
        print("\n❓ COMO JOGAR\n")
        print("Escolha pedra, papel ou tesoura.\n")
        print("Pedra vence tesoura.")
        print("Tesoura vence papel.")
        print("Papel vence pedra.\n")

    elif escolha_menu == 4:
        print("\n👋 Até a próxima!\n")
        jogar = False
