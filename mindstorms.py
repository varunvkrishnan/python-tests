import turtle

def draw_square(some_turtle):
    for i in range (1,5):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_shapes():
    window = turtle.Screen()
    window.bgcolor("red")

    # Turtle 1
    brad = turtle.Turtle()
    brad.color("yellow")
    brad.shape("turtle")
    brad.speed("fast")
    for j in range (1,73):
        brad.left(5)
        draw_square(brad)
        j=j+1
        
    # Turtle 2
    #angie = turtle.Turtle()
    #angie.color("blue")
    #angie.shape("arrow")
    #angie.speed("fast")
    #angie.circle(100)

    # Turtle 3
    #john = turtle.Turtle()
    #john.color("green")
    #john.shape("arrow")
    #john.speed("fast")
    #count=0
    #while count < 3:
    #    john.forward(100)
    #    john.left(120)
    #    count=count+1
        
    window.exitonclick()
draw_shapes()

    
