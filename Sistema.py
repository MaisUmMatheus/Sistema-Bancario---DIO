class ContaBancaria:
    def __init__(self, numero_conta, titular, saldo_inicial=0):
        self.numero_conta = numero_conta
        self.titular = titular
        self.saldo = saldo_inicial
        self.extrato = []

    def depositar(self, quantia):
        if quantia > 0:
            self.saldo += quantia
            self.extrato.append(f"Depósito: +R${quantia}")
            print(f"Depósito de R${quantia} realizado com sucesso!")
        else:
            print("A quantia do depósito deve ser positiva.")

    def sacar(self, quantia):
        if 0 < quantia <= self.saldo:
            self.saldo -= quantia
            self.extrato.append(f"Saque: -R${quantia}")
            print(f"Saque de R${quantia} realizado com sucesso!")
        else:
            print("Saldo insuficiente ou quantia inválida.")

    def transferir(self, outra_conta, quantia):
        if 0 < quantia <= self.saldo:
            self.saldo -= quantia
            outra_conta.saldo += quantia
            self.extrato.append(f"Transferência para {outra_conta.numero_conta}: -R${quantia}")
            outra_conta.extrato.append(f"Transferência de {self.numero_conta}: +R${quantia}")
            print(f"Transferência de R${quantia} para a conta {outra_conta.numero_conta} realizada com sucesso!")
        else:
            print("Saldo insuficiente ou quantia inválida.")

    def verificar_saldo(self):
        print(f"Saldo atual: R${self.saldo}")

    def imprimir_extrato(self):
        print(f"Extrato da conta {self.numero_conta}:")
        for transacao in self.extrato:
            print(transacao)
        print(f"Saldo atual: R${self.saldo}")

class Banco:
    def __init__(self):
        self.contas = {}

    def criar_conta(self, numero_conta, titular, saldo_inicial=0):
        if numero_conta not in self.contas:
            self.contas[numero_conta] = ContaBancaria(numero_conta, titular, saldo_inicial)
            print(f"Conta {numero_conta} criada com sucesso!")
        else:
            print(f"Conta {numero_conta} já existe.")

    def obter_conta(self, numero_conta):
        return self.contas.get(numero_conta, None)

def menu():
    banco = Banco()
    while True:
        print("\nMenu do Banco")
        print("1. Criar nova conta")
        print("2. Depositar")
        print("3. Sacar")
        print("4. Verificar saldo")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            numero_conta = input("Número da conta: ")
            titular = input("Nome do titular: ")
            saldo_inicial = float(input("Saldo inicial: "))
            banco.criar_conta(numero_conta, titular, saldo_inicial)
        elif opcao == "2":
            numero_conta = input("Número da conta: ")
            conta = banco.obter_conta(numero_conta)
            if conta:
                quantia = float(input("Quantia a depositar: "))
                conta.depositar(quantia)
            else:
                print("Conta não encontrada.")
        elif opcao == "3":
            numero_conta = input("Número da conta: ")
            conta = banco.obter_conta(numero_conta)
            if conta:
                quantia = float(input("Quantia a sacar: "))
                conta.sacar(quantia)
            else:
                print("Conta não encontrada.")
        elif opcao == "4":
            numero_conta = input("Número da conta: ")
            conta = banco.obter_conta(numero_conta)
            if conta:
                conta.verificar_saldo()
            else:
                print("Conta não encontrada.")
        elif opcao == "5":
            print("Saindo do sistema bancário.")
            break
        else:
            print("Opção inválida. Tente novamente.")

menu()
