import datetime

def saudacao ():
    print("="*40)
    print("           🤖  PyAssist 🤖")
    print("="*40)
    print("Olá! Eu sou o PyAssist.")
    print("Estou aqui para ajudar você no dia a dia.")
    print("Digite em que posso ajudá-lo ou 'sair' para encerrar.\n")

def receber_comando ():
    comando =  input("Você: ").lower().strip()
    return comando

tarefas = []

def adicionar_tarefa(tarefas):
    tarefa = input("Adicione uma tarefa: ")
    tarefas.append(tarefa)
    print("Tarefa adicionada! ✅")


def listar_tarefas(tarefas):
    print("\n📋 Suas tarefas:")

    for tarefa in tarefas:
        print(f"- {tarefa}")

def processar_comando(comando):

    if "oi" in comando or "olá" in comando:
        print("PyAssist: Olá! Que bom falar com você. 😄")

    elif "tudo bem" in comando:
        print("PyAssist: Tudo ótimo por aqui!")

    elif "seu nome" in comando:
        print("PyAssist: Meu nome é PyAssist. 🤖")

    elif "python" in comando:
        print("PyAssist: Eu fui desenvolvido em Python! 🐍")

    elif "obrigado" in comando or "obrigada" in comando:
        print("PyAssist: Por nada! 😊")

    elif "que horas são" in comando or "horas" in comando:
        horas = datetime.datetime.now()
        formatada= horas.strftime('%H:%Mh')
        print(f"São exatamente: {formatada}")
    elif "que data é hoje" in comando or "data" in comando:
        data= datetime.datetime.now()
        formatada= data.strftime('%d/%m/%Y')
        print(f"Hoje é {formatada}")
    elif "adicionar tarefa" in comando:
        adicionar_tarefa(tarefas)
    elif "minhas tarefas" in comando or "listar tarefas" in comando:
        listar_tarefas(tarefas)
    
    else:
        print("PyAssist: Ainda não sei responder isso. 🤔")


saudacao ()

while True:

    comando = receber_comando ()

    if comando == "sair":
        print("PyAssist: Até mais! 👋")
        break
    processar_comando(comando)

