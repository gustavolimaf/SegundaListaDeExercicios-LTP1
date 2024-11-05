from conta_bancaria import ContaBancaria

class ContaPoupanca(ContaBancaria):
    def __init__(self, numero, titular, saldo=0, taxa_juros=0.01):
        super().__init__(numero, titular, saldo)
        self.taxa_juros = taxa_juros

    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de R${valor:.2f} realizado. Novo saldo: R${self.saldo:.2f}")

    def sacar(self, valor):
        if self.saldo - valor < 0:
            print("Saque recusado: saldo insuficiente para a conta poupança.")
        else:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado. Novo saldo: R${self.saldo:.2f}")

    def calcular_saldo(self):
        return self.saldo

    def calcular_juros(self):
        juros = self.saldo * self.taxa_juros
        self.saldo += juros
        print(f"Juros de R${juros:.2f} aplicados. Novo saldo: R${self.saldo:.2f}")

    def exibir_informacoes(self):
        print(f"Conta Poupança:\nNúmero: {self.numero}\nTitular: {self.titular}\nSaldo: R${self.saldo:.2f}\nTaxa de Juros: {self.taxa_juros * 100:.2f}%")
