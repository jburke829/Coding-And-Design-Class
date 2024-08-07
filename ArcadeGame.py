from tkinter import *
import random

# Making the window
window = Tk()
window.title("The Candy Monster Game")

# Canvas
canvas_width = 400
canvas_height = 400
canvas = Canvas(window, width=canvas_width, height=canvas_height, bg="black")
canvas.pack()

# Welcome Screen
title = canvas.create_text(200,200,text="The Candy Monster",fill="white",font=("Helvetica",20))
directions = canvas.create_text(200,300, text="Collect candy but avoid the red ones", fill="white", font=("Helvetica",15))

# Score Display
score = 0
score_display = Label(window, text="Score: "+ str(score))
score_display.pack()

# Level Display
level = 1
level_display = Label(window, text="Level: "+ str(level))
level_display.pack()

# Player
player_image = PhotoImage(file="greenChar.gif")
mychar = canvas.create_image(200,360, image=player_image)

# Managing Candy Lists
candy_list = []
bad_candy_list = []
candy_speed = 2
candy_diameter = 30
candy_color_list = ["red","yellow","blue","green","purple","pink","white"]

# Making Candy
def make_candy():
    xpos = random.randint(1,canvas_height)
    ypos = 0
    candy_color = random.choice(candy_color_list)
    # (xpos1, ypos1, xpos2, ypos2, color) Oval is created between the 4 positions
    candy = canvas.create_oval(xpos,ypos, xpos+candy_diameter, ypos+candy_diameter, fill=candy_color)
    # Eventually, if a candy is on the bad list, it causes damage
    candy_list.append(candy)
    if candy_color == "red":
        bad_candy_list.append(candy)
    # rescheduling the function
    window.after(1000, make_candy)

def move_candy():
    # Iterating through the list, moving each candy by the candy speed. Candy speed could be changed later if 2 isn't good
    for candy in candy_list:
        canvas.move(candy, 0, candy_speed)
        if canvas.coords(candy)[1] > canvas_height:
            xpos = random.randint(1,canvas_width)
            ypos = 0 
            canvas.coords(candy, xpos, ypos, xpos+30, ypos+30)
    # rescheduling the function
    window.after(50, move_candy)

# function that updates score, level, and candy_speed
def update_score_level():
    global score, level, candy_speed
    score += 1
    score_display.config(text="Score: " + str(score))
    # determine if level change is player has scored 5 points since the last update
    if score % 5 == 0:
        candy_speed += 1
        level += 1
        level_display.config(text="Level: " + str(level))

def end_game_over():
    window.destroy()

def end_title():
    canvas.delete(title)
    canvas.delete(directions)

# Determining Collision in the Game
def collision(item1, item2, distance):
    xdistance = abs(canvas.coords(item1)[0] - canvas.coords(item2)[0])
    ydistance = abs(canvas.coords(item1)[1] - canvas.coords(item2)[1])
    # Checking if the x and y coords are less than the diameter of the shape. If it is, overlap returns as true and can be interpreted as something later
    overlap = xdistance < distance and ydistance < distance
    return overlap

# Checks for Bad Candy and updates the screen and backend items
def check_hits ():
    # Game Over if you hit a bad candy
    for candy in bad_candy_list:
        if collision(mychar, candy, candy_diameter):
            game_over = canvas.create_text(200,200, text="Game Over", fill="red", font=("Helvetica",30))
            window.after(2000,end_game_over)
            return
    # Points and Update if you hit a good candy
    for candy in candy_list:
        if collision(mychar, candy, candy_diameter):
            canvas.delete(candy)
            candy_list.remove(candy)
            update_score_level()
    # How often the game checks for collision
    window.after(100, check_hits)
move_direction = 0

def check_input(event):
    global move_direction
    key = event.keysym
    if key == "Right":
        move_direction = "Right"
    elif key == "Left":
        move_direction = "Left"

def end_input(event):
    global move_direction
    move_direction = "None"

def move_character():
    # Check the input and if your character can legally move past that part of the screen
    if move_direction == "Right" and canvas.coords(mychar)[0] < canvas_width:
        canvas.move(mychar, 10, 0)
    if move_direction == "Left" and canvas.coords(mychar)[0] > 0:
        canvas.move(mychar, -10, 0)
    # Move character at 60FPS    
    window.after(16, move_character)

canvas.bind_all("<KeyPress>", check_input)
canvas.bind_all("<KeyRelease>", end_input)

window.after(1000, end_title)
window.after(1000, make_candy)
window.after(1000, move_candy)
window.after(1000, check_hits)
window.after(1000, move_character)

window.mainloop()