import turtle

class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def posicao(self):
        return (self.x, self.y)

def desenhar_ponto(ponto):
    turtle.penup()
    turtle.goto(ponto.posicao())
    turtle.pendown()
    turtle.dot(10, "red")

while True:
    opcao = input("Digite '1' para inserir coordenadas, ou '2' para encerrar o programa: ")

    if opcao == "1":
        x = float(input("Digite a coordenada x do ponto: "))
        y = float(input("Digite a coordenada y do ponto: "))

        ponto = Ponto(x, y)
        desenhar_ponto(ponto)

    elif opcao == "2":
        print("Encerrando o programa.")
        break
    else:
        print("Opção inválida. Tente novamente.")

turtle.done()
