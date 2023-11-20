import turtle
import time
import random
import pygame

# Instalar
#  pip install pygame
# Inicializar Pygame y el mixer
pygame.init()
pygame.mixer.init()
# Cargar un archivo de sonido (reemplaza 'sound_file.wav' con tu archivo de sonido)
pygame.mixer.music.load("sound.mp3")
# Función para reproducir sonido
def play_sound():
    pygame.mixer.music.play()

# Función para detener el sonido
def stop_sound():
    pygame.mixer.music.stop()

velocidad = 0.05
saltos = 0

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
luz.direction = "stop"

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

def setJugar():
    global creditos
    global velocidad
    global saltos
    if creditos>0:
        creditos = creditos - 1
        texto.clear()
        texto.write("Créditos: {}   Premio: {}".format(creditos, premio), align = "center", font =("Courier", 18, "normal"))
        luz.direction = "right"
        saltos = random.randint(96, 128)
        velocidad = 0.03
        play_sound()


win.listen()
win.onkeypress(setCoins, 'c')
win.onkeypress(setJugar, 'j')


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
def check_saltos():
    global saltos
    global velocidad
    if saltos == 0:
        luz.direction = "stop"
        stop_sound()
    else:
        saltos = saltos - 1
        if(saltos%8==0):
            velocidad = velocidad + 0.01

while True:
    check_saltos()
    win.update()
    mov()    
    time.sleep(velocidad)


