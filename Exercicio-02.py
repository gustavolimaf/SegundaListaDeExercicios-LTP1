class Motor:
    def __init__(self, tipo="V6", potencia=300):
        self.tipo = tipo
        self.potencia = potencia
        self.ligado = False

    def ligar(self):
        self.ligado = True
        print("O motor foi ligado.")

    def desligar(self):
        self.ligado = False
        print("O motor foi desligado.")

    def status(self):
        return f"Motor: {self.tipo} com {self.potencia} CV - {'Ligado' if self.ligado else 'Desligado'}"


class Pneu:
    def __init__(self, tipo="Radial", pressao=32):
        self.tipo = tipo
        self.pressao = pressao
        self.condicao = "Boa" if pressao >= 30 else "Baixa"

    def calibrar(self, pressao):
        self.pressao = pressao
        self.condicao = "Boa" if pressao >= 30 else "Baixa"
        print(f"Pneu calibrado para {self.pressao} PSI.")

    def status(self):
        return f"Pneu: {self.tipo} com pressão de {self.pressao} PSI - Condição: {self.condicao}"


class Veiculo(Motor, Pneu):
    def __init__(self, nome="Carro Esportivo"):
        Motor.__init__(self)
        Pneu.__init__(self)
        self.nome = nome

    def status(self):
        status_motor = Motor.status(self)
        status_pneu = Pneu.status(self)
        return f"\n{self.nome} Status:\n{status_motor}\n{status_pneu}"


def menu():
    veiculo = Veiculo()
    while True:
        print("\n=== Menu do Veículo ===")
        print("1. Ligar o motor")
        print("2. Desligar o motor")
        print("3. Calibrar o pneu")
        print("4. Ver status do veículo")
        print("5. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            veiculo.ligar()
        elif escolha == "2":
            veiculo.desligar()
        elif escolha == "3":
            pressao = float(input("Digite a pressão desejada para o pneu (em PSI): "))
            veiculo.calibrar(pressao)
        elif escolha == "4":
            print(veiculo.status())
        elif escolha == "5":
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

menu()