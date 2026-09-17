print("-"*40)
print("             🤖PyAssist")
print("-"*40)

print("Olá! Eu sou o PyAssist.")
print("Estou aqui para ajudar você no dia a dia.")
print("Digite 'sair' para encerrar.\n")

while True:

    mensagem =  input("Você: ").lower().strip()

    if mensagem == "sair":
        print("PyAssist: Até mais! 👋")
        break

    elif "oi" in mensagem or "olá" in mensagem:
        print("PyAssist: Olá! Que bom falar com você. 😄")

    elif "tudo bem" in mensagem:
        print("PyAssist: Tudo ótimo por aqui! E com você?")

    elif "seu nome" in mensagem:
        print("PyAssist: Meu nome é PyAssist. 🤖")

    elif "obrigado" in mensagem or "obrigada" in mensagem:
        print("PyAssist: Por nada! 😊")

    else:
        print("PyAssist: Ainda não sei responder isso, mas podemos me ensinar!")