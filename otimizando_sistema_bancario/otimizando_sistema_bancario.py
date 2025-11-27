import textwrap
from abc import ABC, abstractmethod
from datetime import datetime


class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def executar_transacao(self, conta, operacao):
        operacao.registrar(conta)

    def vincular_conta(self, conta):
        self.contas.append(conta)


class PessoaFisica(Cliente):
    def __init__(self, nome, nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.nascimento = nascimento
        self.cpf = cpf


class Conta:
    def __init__(self, numero, cliente):
        self._agencia = "0001"
        self._numero = numero
        self._cliente = cliente
        self._saldo = 0
        self._historico = Historico()

    @classmethod
    def criar(cls, cliente, numero):
        return cls(numero, cliente)

    @property
    def agencia(self):
        return self._agencia

    @property
    def numero(self):
        return self._numero

    @property
    def cliente(self):
        return self._cliente

    @property
    def saldo(self):
        return self._saldo

    @property
    def historico(self):
        return self._historico

    def sacar(self, valor):
        if valor > self._saldo:
            print("\n*** Operação falhou! Saldo insuficiente. ***")
            return False

        if valor <= 0:
            print("\n*** Valor de saque inválido. ***")
            return False

        self._saldo -= valor
        print("\n=== Saque realizado com sucesso! ===")
        return True

    def depositar(self, valor):
        if valor <= 0:
            print("\n*** Depósito inválido. ***")
            return False

        self._saldo += valor
        print("\n=== Depósito realizado! ===")
        return True


class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, max_saques=3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.max_saques = max_saques

    def sacar(self, valor):
        saques_realizados = len([
            t for t in self.historico.transacoes
            if t["tipo"] == Saque.__name__
        ])

        if valor > self.limite:
            print("\n*** Saque excede o limite permitido. ***")
            return False

        if saques_realizados >= self.max_saques:
            print("\n*** Limite diário de saques atingido. ***")
            return False

        return super().sacar(valor)

    def __str__(self):
        return f"""
        Agência:\t{self.agencia}
        Conta:\t\t{self.numero}
        Titular:\t{self.cliente.nome}
        """


class Historico:
    def __init__(self):
        self._registro = []

    @property
    def transacoes(self):
        return self._registro

    def adicionar(self, operacao):
        self._registro.append({
            "tipo": operacao.__class__.__name__,
            "valor": operacao.valor,
            "data": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        })


class Transacao(ABC):
    @property
    @abstractmethod
    def valor(self):
        ...

    @abstractmethod
    def registrar(self, conta):
        ...


class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        if conta.sacar(self.valor):
            conta.historico.adicionar(self)


class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        if conta.depositar(self.valor):
            conta.historico.adicionar(self)


def menu():
    opcoes = """
    ======== MENU PRINCIPAL ========
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Nova conta
    [5] Listar contas
    [6] Novo cliente
    [0] Sair
    => """
    return input(textwrap.dedent(opcoes))


def localizar_cliente(cpf, lista):
    filtrados = [c for c in lista if c.cpf == cpf]
    return filtrados[0] if filtrados else None


def selecionar_conta(cliente):
    if not cliente.contas:
        print("\n*** O cliente não possui contas. ***")
        return None
    return cliente.contas[0]


def operacao_deposito(clientes):
    cpf = input("CPF do cliente: ")
    cliente = localizar_cliente(cpf, clientes)

    if not cliente:
        print("\n*** Cliente não encontrado. ***")
        return

    conta = selecionar_conta(cliente)
    if not conta:
        return

    valor = float(input("Valor para depósito: "))
    cliente.executar_transacao(conta, Deposito(valor))


def operacao_saque(clientes):
    cpf = input("CPF do cliente: ")
    cliente = localizar_cliente(cpf, clientes)

    if not cliente:
        print("\n*** Cliente não encontrado. ***")
        return

    conta = selecionar_conta(cliente)
    if not conta:
        return

    valor = float(input("Valor para saque: "))
    cliente.executar_transacao(conta, Saque(valor))


def mostrar_extrato(clientes):
    cpf = input("CPF do cliente: ")
    cliente = localizar_cliente(cpf, clientes)

    if not cliente:
        print("\n*** Cliente não encontrado. ***")
        return

    conta = selecionar_conta(cliente)
    if not conta:
        return

    print("\n======= EXTRATO =======")
    if not conta.historico.transacoes:
        print("Nenhuma movimentação registrada.")
    else:
        for t in conta.historico.transacoes:
            print(f"{t['tipo']}: R$ {t['valor']:.2f} - {t['data']}")

    print(f"\nSaldo atual: R$ {conta.saldo:.2f}")
    print("========================")


def cadastrar_cliente(clientes):
    cpf = input("CPF: ")

    if localizar_cliente(cpf, clientes):
        print("\n*** Já existe cliente com esse CPF. ***")
        return

    nome = input("Nome completo: ")
    nasc = input("Data de nascimento (dd/mm/aaaa): ")
    endereco = input("Endereço completo: ")

    novo = PessoaFisica(nome, nasc, cpf, endereco)
    clientes.append(novo)

    print("\n=== Cliente cadastrado com sucesso! ===")


def cadastrar_conta(num, clientes, contas):
    cpf = input("CPF do cliente: ")
    cliente = localizar_cliente(cpf, clientes)

    if not cliente:
        print("\n*** Cliente não encontrado. ***")
        return

    nova = ContaCorrente.criar(cliente, num)
    contas.append(nova)
    cliente.vincular_conta(nova)

    print("\n=== Conta criada com sucesso! ===")


def listar_contas(contas):
    for conta in contas:
        print("=" * 60)
        print(textwrap.dedent(str(conta)))


def main():
    clientes = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "1":
            operacao_deposito(clientes)

        elif opcao == "2":
            operacao_saque(clientes)

        elif opcao == "3":
            mostrar_extrato(clientes)

        elif opcao == "6":
            cadastrar_cliente(clientes)

        elif opcao == "4":
            numero = len(contas) + 1
            cadastrar_conta(numero, clientes, contas)

        elif opcao == "5":
            listar_contas(contas)

        elif opcao == "0":
            break

        else:
            print("\n*** Opção inválida. ***")


main()
