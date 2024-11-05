from conta_bancaria import ContaBancaria

class ContaCorrente(ContaBancaria):
    def __init__(self, numero, titular, saldo=0, limite_cheque_especial=500):
        super().__init__(numero, titular, saldo)
        self.limite_cheque_especial = limite_cheque_especial

    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de R${valor:.2f} realizado. Novo saldo: R${self.saldo:.2f}")

    def sacar(self, valor):
        if self.saldo - valor < -self.limite_cheque_especial:
            print("Saque recusado: saldo insuficiente com limite de cheque especial.")
        else:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado. Novo saldo: R${self.saldo:.2f}")

    def calcular_saldo(self):
        return self.saldo

    def exibir_informacoes(self):
        print(f"Conta Corrente:\nNúmero: {self.numero}\nTitular: {self.titular}\nSaldo: R${self.saldo:.2f}\nLimite de Cheque Especial: R${self.limite_cheque_especial:.2f}")
