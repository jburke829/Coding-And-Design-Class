import turtle

shelly = turtle.Turtle()
shelly.shape('turtle')

colors = ['red','blue','yellow','green','pink','black']

for i in range(6):
    shelly.begin_fill()
    shelly.color(colors[i])
    for j in range(4):
        shelly.forward(100)
        shelly.left(90)
    shelly.end_fill()
    shelly.left(60)
    
shelly.end_fill()
