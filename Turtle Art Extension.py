import turtle

shelly = turtle.Turtle()
shelly.speed(0)
turtle.bgcolor('black')
colors = ['red','orange','yellow','green','blue','purple']

shelly.color('yellow')
def squareSpiral():
    shelly.speed(0)
    for i in range(100):
        shelly.forward(i*5)
        shelly.right(90)

def circleCircles():
    shelly.speed(0)
    for i in range(36):
        shelly.penup()
        shelly.forward(150)
        for i in range(6):
            shelly.pendown()
            shelly.color(colors[i])
            shelly.circle((i+1)*1.5)
            shelly.penup()
            shelly.forward(20)
        shelly.backward(270)
        shelly.right(10)
        
squareSpiral()
shelly.reset()
circleCircles()