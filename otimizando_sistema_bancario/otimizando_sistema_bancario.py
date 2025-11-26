def exibir_menu_principal():
    print("\n========= SISTEMA BANCÁRIO =========")
    print("1 - Fazer depósito")
    print("2 - Fazer saque")
    print("3 - Consultar extrato")
    print("4 - Registrar novo usuário")
    print("5 - Criar nova conta bancária")
    print("6 - Mostrar todas as contas")
    print("0 - Encerrar")
    return input("Escolha uma opção: ")


def operacao_deposito(saldo_atual, registros):
    try:
        valor = float(input("Informe o valor para depósito: "))
    except ValueError:
        print("Valor inválido.")
        return saldo_atual, registros

    if valor <= 0:
        print("Depósito não permitido.")
        return saldo_atual, registros

    saldo_atual += valor
    registros.append(("Depósito", valor))
    print("Depósito realizado com sucesso.")
    return saldo_atual, registros


def operacao_saque(
    saldo_atual,
    registros,
    limite_por_operacao,
    quantidade_saques,
    limite_diario
):

    try:
        valor = float(input("Informe o valor para saque: "))
    except ValueError:
        print("Valor inválido.")
        return saldo_atual, registros, quantidade_saques

    if quantidade_saques >= limite_diario:
        print("Limite diário de saques atingido.")
        return saldo_atual, registros, quantidade_saques

    if valor <= 0:
        print("O valor para saque deve ser positivo.")
        return saldo_atual, registros, quantidade_saques

    if valor > limite_por_operacao:
        print("O valor ultrapassa o limite permitido por saque.")
        return saldo_atual, registros, quantidade_saques

    if valor > saldo_atual:
        print("Saldo insuficiente.")
        return saldo_atual, registros, quantidade_saques

    saldo_atual -= valor
    registros.append(("Saque", valor))
    quantidade_saques += 1
    print("Saque concluído.")
    return saldo_atual, registros, quantidade_saques


def mostrar_extrato(saldo_atual, registros):
    print("\n============ EXTRATO ============")
    if not registros:
        print("Nenhuma movimentação registrada.")
    else:
        for tipo, valor in registros:
            print(f"{tipo}: R$ {valor:.2f}")
    print(f"Saldo atual: R$ {saldo_atual:.2f}")
    print("==================================")


def buscar_usuario_por_codigo(unico, lista):
    for usuario in lista:
        if usuario["cpf"] == unico:
            return usuario
    return None


def registrar_novo_usuario(lista_usuarios):
    codigo = input("Digite o CPF do usuário: ")

    if buscar_usuario_por_codigo(codigo, lista_usuarios):
        print("Já existe um usuário cadastrado com este CPF.")
        return

    nome = input("Nome completo: ")
    nascimento = input("Data de nascimento (dd-mm-aaaa): ")
    endereco = input("Endereço completo: ")

    lista_usuarios.append({
        "cpf": codigo,
        "nome": nome,
        "data_nascimento": nascimento,
        "endereco": endereco
    })

    print("Usuário registrado.")


def criar_nova_conta(agencia, lista_usuarios, lista_contas):
    codigo = input("CPF do titular da conta: ")
    usuario_encontrado = buscar_usuario_por_codigo(codigo, lista_usuarios)

    if usuario_encontrado is None:
        print("Usuário não encontrado. Conta não criada.")
        return

    numero_conta = len(lista_contas) + 1
    conta = {
        "agencia": agencia,
        "conta": numero_conta,
        "titular": usuario_encontrado
    }
    lista_contas.append(conta)

    print("Conta criada com sucesso.")


def mostrar_contas_registradas(lista_contas):
    if not lista_contas:
        print("Nenhuma conta cadastrada.")
        return

    print("\n========== CONTAS REGISTRADAS ==========")
    for conta in lista_contas:
        print(f"Agência: {conta['agencia']}")
        print(f"Número da conta: {conta['conta']}")
        print(f"Titular: {conta['titular']['nome']}")
        print("----------------------------------------")


def iniciar_sistema_bancario():

    saldo = 0.0
    limite_saque = 500
    historico_movimentacoes = []
    total_saques_realizados = 0
    limite_diario_saques = 3

    usuarios = []
    contas = []

    agencia_padrao = "0001"

    while True:
        escolha = exibir_menu_principal()

        if escolha == "1":
            saldo, historico_movimentacoes = operacao_deposito(saldo, historico_movimentacoes)

        elif escolha == "2":
            saldo, historico_movimentacoes, total_saques_realizados = operacao_saque(
                saldo,
                historico_movimentacoes,
                limite_saque,
                total_saques_realizados,
                limite_diario_saques
            )

        elif escolha == "3":
            mostrar_extrato(saldo, historico_movimentacoes)

        elif escolha == "4":
            registrar_novo_usuario(usuarios)

        elif escolha == "5":
            criar_nova_conta(agencia_padrao, usuarios, contas)

        elif escolha == "6":
            mostrar_contas_registradas(contas)

        elif escolha == "0":
            print("Encerrando o sistema...")
            break

        else:
            print("Opção inválida.")


iniciar_sistema_bancario()
