from conta_corrente import ContaCorrente
from conta_poupanca import ContaPoupanca

def menu_interativo():
    tipo_conta = input("Digite '1' para Conta Corrente ou '2' para Conta Poupança: ")

    if tipo_conta == "1":
        numero = input("Digite o número da conta: ")
        titular = input("Digite o nome do titular: ")
        conta = ContaCorrente(numero, titular)
    elif tipo_conta == "2":
        numero = input("Digite o número da conta: ")
        titular = input("Digite o nome do titular: ")
        conta = ContaPoupanca(numero, titular)
    else:
        print("Opção inválida. Encerrando o programa.")
        return

    while True:
        print("\n=== Menu da Conta ===")
        print("1. Depositar")
        print("2. Sacar")
        print("3. Exibir informações da conta")
        if isinstance(conta, ContaPoupanca):
            print("4. Calcular juros")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            valor = float(input("Digite o valor a ser depositado: "))
            conta.depositar(valor)
        elif opcao == "2":
            valor = float(input("Digite o valor a ser sacado: "))
            conta.sacar(valor)
        elif opcao == "3":
            conta.exibir_informacoes()
        elif opcao == "4" and isinstance(conta, ContaPoupanca):
            conta.calcular_juros()
        elif opcao == "5":
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu_interativo()
