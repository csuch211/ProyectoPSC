from turtle import Turtle, Screen
from random import randint, choice

#Setup inicial de la pantalla

ventana = Screen()
ventana.title("Mi primera carrera de tortugas")
ventana.setup(500, 500)

mis_tortugas = list()
colores = ["red","orange","gold","green","darkcyan","blue","purple"]
apuesta = ventana.textinput("Haga su apuesta", f"Que tortuga ganara? {colores}")
base = -160
for color in colores:
    tortuga = Turtle(shape="turtle")
    tortuga.color(color)
    tortuga.penup()
    tortuga.setpos(x= -230,y=base)
    base = base + 50
    mis_tortugas.append((tortuga))

comenzo = True

while comenzo:
    pasos = randint(2, 10)
    tortuga = choice(mis_tortugas)
    tortuga.forward(pasos)

    if tortuga.xcor() > 230:
        comenzo = False

        if apuesta == tortuga.pencolor():
            print("Tu tortuga ha ganado")
        else:
            print("Has perdido")





ventana.exitonclick()