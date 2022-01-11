import turtle
import random
t=turtle.Turtle()
t.speed(0)
turtle.bgcolor('black')

class C():
    def podpis(self):
        t.penup()
        t.goto(450,450)
        t.write(f"Karol Bułdak, \n ZZISS1-1111", font=('Comic Sans', 25, 'bold'))
        t.goto(0,0)
        
    def gwiazdki(self, x, y, size, color):
        t.penup()
        t.goto(x,y)
        t.color(color)
        for j in range(4):
            for i in range(5):
                t.pendown()
                t.forward(size)
                t.right(144)
            t.penup()
            t.forward(220)
            
    def glowy(self, x, y, size, color):
        t.color(color)
        t.penup()
        t.goto(x,y)
        for j in range(4):
            t.pendown()
            t.circle(size)
            t.penup()
            t.forward(210)
        t.goto(0,0)
    
    def ciala(self, x, y, height, color):
        t.color(color)
        t.penup()
        t.goto(x,y)
        for i in range(4):
            t.begin_fill()
            for j in range(4):
                t.pendown()
                t.forward(100)
                t.right(90)
                t.forward(height)
            t.end_fill()
            t.penup()
            t.forward(210)
            
    def oczy(self, x, y, size, color):
        t.color(color)
        t.penup()
        t.goto(x,y)
        t.pensize(10)
        for j in range(4):
            t.pendown()
            t.circle(size)
            t.penup()
            t.forward(200)
        t.goto(x+30,y)
        for j in range(4):
            t.pendown()
            t.circle(size)
            t.penup()
            t.forward(200)

            
    def trawa(self):
        t.penup()
        t.color('green')
        t.begin_fill()
        t.goto(-600,-250)
        for j in range(4):
                t.pendown()
                t.forward(10000)
                t.right(90)
                t.forward(100)
        t.end_fill()
        
    def czapki(self, x, y, size, color):

        t.color(color)
        t.penup()
        t.goto(x,y)
        for i in range(4):
            t.begin_fill()
            t.pendown()
            t.left(90)
            t.circle(size, 180)
            t.left(90)
            t.forward(2*size)
            t.penup()
            t.forward(210)
            t.penup()
            t.end_fill()
    
    def kwiatki(self, x, y, size, color):
        t.penup()
        t.goto(x,y)
        t.color(color)
        for w in range(4):
            for j in range(4):
                t.begin_fill()
                for i in range(2):
                    t.pendown()
                    t.circle(size,90)
                    t.circle(size//2,90)
                t.right(90)
                t.end_fill()
            t.penup()
            t.forward(200)
    
    def rysunek(self):
        zolw.trawa()
        zolw.kwiatki(-500, -400, 20, 'yellow')
        zolw.kwiatki(-350, -300, 20, 'yellow')
        zolw.kwiatki(-600, -500, 20, 'violet')
        zolw.kwiatki(0, -450, 20, 'violet')
        zolw.ciala(-300, -50, 100, 'blue')
        zolw.gwiazdki(-400, 400, 200, 'yellow')
        zolw.glowy(-300,-50,50,'white')
        zolw.czapki(-225, 25, 70, 'white')
        zolw.oczy(-300, -10, 10, 'white')
        zolw.podpis()
        t.hideturtle()
        

            
         
zolw=C()
zolw.rysunek()


