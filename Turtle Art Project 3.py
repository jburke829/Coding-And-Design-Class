import turtle

shelly = turtle.Turtle()
shelly.shape('turtle')
turtle.bgcolor('black')
shelly.speed(0)

colors = ['red','orange','yellow','green','blue','red']
for n in range(36):
    for i in range(6):
        shelly.color(colors[i])
        shelly.forward(100)
        shelly.left(60)
    shelly.right(10)
shelly.penup()
shelly.color('white')
for i in range(36):
    shelly.forward(220)
    shelly.pendown()
    shelly.circle(5)
    shelly.penup()
    shelly.backward(220)
    shelly.right(10)