import turtle
import time

posponer = 0.05
creditos = 0
premio = 0
#Pantalla (Ventana)

win = turtle.Screen()
win.title("Frutas Coins")
win.bgcolor("black")
win.setup(width=400, height=700)
win.tracer(0)

#Punto que juega
luz = turtle.Turtle()
luz.speed(0)
luz.shape("square")
luz.color("red")
luz.penup()#Quitar rastro
luz.goto(0, -250)
luz.direction = "right"

#Texto
texto = turtle.Turtle()
texto.speed(0)
texto.color("red")
texto.penup()
texto.hideturtle()
texto.goto(0, 290)
texto.write("Créditos: {}   Premio: {}".format(creditos, premio), align = "center", font =("Courier", 18, "normal"))


#Leer Teclado
def setCoins():
    global creditos
    creditos =  creditos + 1
    texto.clear()
    texto.write("Créditos: {}   Premio: {}".format(creditos, premio), align = "center", font =("Courier", 18, "normal"))
    
win.listen()
win.onkeypress(setCoins, 'c')


#Mover
def mov():
    if luz.direction == "up":
        y = luz.ycor()
        if(y<250):
            luz.sety(y + 50)
        else:
            luz.direction = "left"
    if luz.direction == "down":
        y = luz.ycor()
        if(y>-250):
            luz.sety(y - 50)
        else:
            luz.direction = "right"
    if luz.direction == "left":
        x = luz.xcor()
        if(x>-150):
            luz.setx(x - 50)
        else:
            luz.direction = "down"
    if luz.direction == "right":
        x = luz.xcor()
        if(x<150):
            luz.setx(x + 50)
        else:
            luz.direction = "up"
            
while True:
    win.update()
    mov()
    time.sleep(posponer)
