import turtle

def draw_square(brad):
    #window = turtle.Screen()
    #window.bgcolor("red")
    #brad = turtle.Turtle()
    brad.shape("circle")
    brad.color("yellow")
    brad.speed("slow")
    
    i = 0
    while i<4:  # for i in range(1,5):
        brad.forward(100)
        brad.right(90)
        i = i + 1

    #window.exitonclick()

def draw_circle(angie):
    #window = turtle.Screen()
    #window.bgcolor("red")
    #angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("green")
    angie.circle(100)
    #window.exitonclick()

def draw_triangle(tri):
    #window = turtle.Screen()
    #window.bgcolor("red")
    #tri = turtle.Turtle()
    tri.shape("square")
    tri.color("blue")

    i = 0
    while i < 3 :
        tri.forward(100)
        tri.right(120)
        i += 1

    
    

def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")
    angie = turtle.Turtle()
    draw_square(angie)
    draw_circle(angie)
    draw_triangle(angie)
    window.exitonclick()


#draw_art()


def draw_square_in_circle():
    window = turtle.Screen()
    window.bgcolor("red")
    angie = turtle.Turtle()
    for i in range(1,37):
        i += 1
        draw_square(angie)
        angie.right(10)
    window.exitonclick()

draw_square_in_circle()         
