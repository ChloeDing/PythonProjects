import turtle

def draw_name_initial():
    canvas = turtle.Screen()
    canvas.bgcolor("green")

    angie = turtle.Turtle()

    angie.shape("turtle")
    angie.color("black")

# version 1:
    angie.penup()
    angie.setx(-200)
    angie.sety(200)
    angie.pendown()
    
    angie.right(90)
    angie.forward(100)
    angie.left(90)
    angie.circle(50, 180)

    angie.penup()
    angie.setx(-100)
    angie.pendown()

    angie.left(90)
    angie.forward(100)
    angie.left(90)
    angie.forward(50)

# version 2:
    angie.penup()
    angie.setx(-200)
    angie.sety(-200)
    angie.pendown()

    angie.right(90)
    angie.forward(100)
    angie.left(90)
    angie.forward(100)
    angie.left(135)
    angie.forward(141)

    angie.penup()
    angie.setx(-100)
    angie.sety(-300)
    angie.pendown()
    angie.right(90)
    angie.circle(70, 180)

    
    angie.penup()
    angie.setx(0)
    angie.sety(0)
    angie.pendown()
    canvas.exitonclick()

draw_name_initial()
    
