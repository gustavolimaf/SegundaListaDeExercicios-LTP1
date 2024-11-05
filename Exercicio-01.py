import turtle as t

class Forma:
    def desenhar(self):
        pass

class Triangulo(Forma):
    def desenhar(self):
        t.color("green")
        t.pensize(5)
        t.penup()
        t.goto(-50, -50)
        t.pendown()
        for _ in range(3):
            t.forward(100)
            t.left(120)

class Circulo(Forma):
    def desenhar(self):
        t.color("blue")
        t.pensize(5)
        t.penup()
        t.goto(0, -50)
        t.pendown()
        t.circle(50)

class Quadrado(Forma):
    def desenhar(self):
        t.color("purple")
        t.pensize(5)
        t.penup()
        t.goto(-50, -50)
        t.pendown()
        for _ in range(4):
            t.forward(100)
            t.left(90)

def desenhar_formas():
    forma = Triangulo()
    forma.desenhar()
    t.clearscreen()

    forma = Circulo()
    forma.desenhar()
    t.clearscreen()

    forma = Quadrado()
    forma.desenhar()
    t.done()

desenhar_formas()
