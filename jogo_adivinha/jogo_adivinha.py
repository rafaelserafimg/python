import random

print("-"*34)
print("     🎮 JOGO DE ADIVINHA 🎮")
print("     ❤️   TENTATIVAS = 5  ❤️")
print("-"*34)

escolha_cpu = random.randint(0,20)
tentativa = 0

while True:
   
    
    print("Escolha um número de 0 a 20.")
    jogador = int(input("Digite seu palpite: "))
    
    if jogador < 0 or jogador > 20:
      print("Número inválido! Escolha de 0 a 20!\n")
      continue
    tentativa = tentativa + 1

    if jogador == escolha_cpu:
       print("🎯 Parabéns! Você acertou!")
       print(f"Você precisou de {tentativa} tentativas.\n")
       break
    elif jogador < escolha_cpu:
       print("O número secreto é maior!\n")
    else:
       print("O número secreto é menor!\n")

    if tentativa == 5:
        print("\nVocê atingiu o máximo de tentativas!")
        print(f"❌ Você perdeu! O número secreto era {escolha_cpu}.\n")
        break