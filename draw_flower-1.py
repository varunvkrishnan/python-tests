import turtle

window=turtle.Screen()
window.bgcolor("black")

objCircle = turtle.Turtle()
objCircle.shape("classic")
objCircle.color("white")
objCircle.speed("fastest")

for i in range(1,50):  
    objCircle.left(45)
    objCircle.forward(50)
    objCircle.right(45)
    objCircle.forward(50)
    objCircle.right(135)
    objCircle.forward(50)
    objCircle.right(45)
    objCircle.forward(50)
    objCircle.left(10)
    
objCircle.seth(270)
objCircle.forward(200)

window.exitonclick()
