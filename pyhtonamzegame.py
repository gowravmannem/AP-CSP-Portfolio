import turtle
import math
import random
import time

class Key(turtle.Turtle):
    def __init__(self,x,y):
        turtle.Turtle.__init__(self)
        self.penup()
        self.goto(x,y)
        self.speed(0)
        self.color("green")
        
    def materialize(self):
        self.hideturtle()
        self.goto(2500,2500)
        

class Enemy(turtle.Turtle):
    def __init__(self,x,y):
        turtle.Turtle.__init__(self)
        self.speed(0)
        self.penup()
        self.goto(x,y)
        self.shape("triangle")
        self.color("purple")

    def move(self):
        self.direction=random.randint(1,4)
        if self.direction == 1:
            movex=self.xcor()
            movey=self.ycor()+24
        elif self.direction == 2:
            movex=self.xcor()
            movey=self.ycor()-24
        elif self.direction == 3:
            movex=self.xcor()-24
            movey=self.ycor()
        elif self.direction == 4:
            movex=self.xcor()+24
            movey=self.ycor()
        if (movex,movey) not in walls_loc:
            self.goto(movex,movey)
        else:
            self.direction=random.randint(1,4)
        screen.ontimer(self.move,random.randint(100,400))
    
    def materialize(self):
        self.hideturtle()
        self.goto(-2500,-2500)
        

def createmaze(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            letter=level[y][x]
            screenxcor=-288+(x*24)
            screenycor=288-(y*24)
            if letter == "w":
                wall.goto(screenxcor,screenycor)
                wall.stamp()
                walls_loc.append((screenxcor,screenycor))
            elif letter == "p":
                player.goto(screenxcor,screenycor)
            elif letter == "k":
                keys_loc.append(Key(screenxcor,screenycor))
            elif letter == "e":
                enemies_loc.append(Enemy(screenxcor,screenycor))
            elif letter == "g":
                gate.goto(screenxcor,screenycor)

def moveup():
    movex=player.xcor()
    movey=player.ycor()+24
    if (movex,movey) not in walls_loc:
        player.goto(movex,movey)

def movedown():
    movex=player.xcor()
    movey=player.ycor()-24
    if (movex,movey) not in walls_loc:
        player.goto(movex,movey)

def moveright():
    movex=player.xcor()+24
    movey=player.ycor()
    if (movex,movey) not in walls_loc:
        player.goto(movex,movey)

def moveleft():
    movex=player.xcor()-24
    movey=player.ycor()
    if (movex,movey) not in walls_loc:
        player.goto(movex,movey)

def collision(thing):
    delta_xcor=player.xcor()-thing.xcor()
    delta_ycor=player.ycor()-thing.ycor()
    diag_length=math.sqrt((delta_xcor**2)+(delta_ycor**2))
    if diag_length <= 6:
        return True
    else:
        return False

def playercontrol():
    screen.onkey(moveleft,"Left")
    screen.onkey(movedown,"Down")
    screen.onkey(moveup,"Up")
    screen.onkey(moveright,"Right")
    screen.listen()

def moveallenemies():
    for enemy in enemies_loc:
        enemy.move()
        screen.update()
    if enemies_loc:
        screen.ontimer(moveallenemies,100)
    else:
        screen.tracer(True)

def intro():
    print("Welcome to DungeonEscape!!")
    userpref=int(input("Enter 1 to start game or 0 to quit"))
    if userpref==1:
      return True
    elif userpref==0:
      return False

def instructions():
    print("You have to get four keys and open the gate")
    time.sleep(2)
    print("The gate will NOT open until you have all keys")
    time.sleep(2)
    print("The purple enemies will tase you if you get too close.")
    time.sleep(2)
    print("You can live to be tased 5 times")
    time.sleep(2)
    print("Use the arrows keys to move")
    time.sleep(2)
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
    print("Go!!!")

screen=turtle.Screen()
screen.bgcolor("white")
screen.setup(700,700)

wall=turtle.Turtle()
wall.shape("square")
wall.color("black")
wall.penup()
wall.speed(0)

gate=turtle.Turtle()
gate.shape("square")
gate.color("blue")
gate.penup()
gate.speed(0)

player=turtle.Turtle()
player.shape("circle")
player.color("red")
player.penup()
player.speed(0)
player.key=0
player.lives=5

layout=[
"wwwwwwwwwwwwwwwwwwwwwwwww",
"wp  wwwwwwwwwwwwwwwwwwwww",
"ww                   wwww",
"wwwwwwwwwwwwwwwwwwe   www",
"w                   kwwww",
"w   wwwwwwwwwwwwwwwwwwwww",
"w   w                  ww",
"w  ew w   wwwwwwwwwwe  ww",
"w   wkw   ww           ww",
"w   www   ww  wwwwwwwwwww",
"w         ww           ww",
"wwwwwwwwwwwwwwwwwwwwwe ww",
"w                      ww",
"w  wwwwwwwwwwwwwwwwwwwwww",
"w ewk                   w",
"w  www   wwwwwwwwwwwwwe w",
"w        ww             w",
"wwwwwwwwww      wwwwwwwww",
"w       w   ww   wwwwwwww",
"w   ww     wwww         w",
"w   wwwwwwwwwwwwwwwww   w",
"w  ew       ww      we  w",
"w   wkwwww  ww  ww gw   w",
"w   wwwwww  ww  wwwww   w",
"w           ww          w",
"wwwwwwwwwwwwwwwwwwwwwwwww",
]

keys_loc=[]
enemies_loc=[]
walls_loc=[]

if intro():
    screen.tracer(5)
    createmaze(layout)
    moveallenemies()
    instructions()
    playercontrol()
else:
    print("Alright have a good day")

while True:
    for key in keys_loc:
        if collision(key):
            player.key+=1
            key.materialize()
            keys_loc.remove(key)
    for enemy in enemies_loc:
        if collision(enemy):
            enemy.materialize()
            enemies_loc.remove(enemy)
            player.lives-=1
            print("Lost 1 life.",player.lives,"lives remaining")
    screen.update()
    if player.lives==0:
        print("You have died")
        screen.clear()
        break
    if collision(gate) and player.key==4:
        print("You have won!!! Great Job!!!")
        screen.clear()
        break