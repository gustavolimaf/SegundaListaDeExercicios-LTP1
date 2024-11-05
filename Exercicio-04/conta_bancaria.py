from abc import ABC, abstractmethod

class ContaBancaria(ABC):
    def __init__(self, numero, titular, saldo=0):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo

    @abstractmethod
    def depositar(self, valor):
        pass

    @abstractmethod
    def sacar(self, valor):
        pass

    @abstractmethod
    def calcular_saldo(self):
        pass

    @abstractmethod
    def exibir_informacoes(self):
        pass
