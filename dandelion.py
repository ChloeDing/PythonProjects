import turtle

def draw_diamond(angie):
    angie.shape("turtle")
    angie.color("white")
    angie.left(120)
    angie.forward(50)
    angie.right(60)
    angie.forward(50)
    angie.right(120)
    angie.forward(50)
    angie.right(60)
    angie.forward(50)
    angie.left(120)
    


def draw_a_dandelion():
    canvas = turtle.Screen()
    canvas.bgcolor("green")

    angie = turtle.Turtle()

    for i in range(1, 37):
        draw_diamond(angie)
        angie.right(10)

    angie.right(90)
    angie.forward(150)

    canvas.exitonclick()


draw_a_dandelion()
    
