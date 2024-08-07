from tkinter import *
import random
from time import sleep

# Making the window
window = Tk()
window.title("Password Generator")

# Canvas
canvas_width = 600
canvas_height = 400
canvas = Canvas(window, width=canvas_width, height=canvas_height, bg="black")
canvas.pack()

# Welcome Screen

title = canvas.create_text(canvas_width/2, canvas_height*2/3, text="Password Generator",fill="white",font=("Helvetica",20))
directions = canvas.create_text(canvas_width/2, canvas_height * 1/3, text="Press the button below if you want a new password", fill="white", font=("Helvetica",15))


# Password Generation

secret =""
def make_password():
    global secret
    
    canvas.delete(secret)
    canvas.delete(title)
    canvas.delete(directions)
   
    # Getting words from words.txt
    inp = open("words.txt")    
    lines=inp.read().split("\n")
    inp.close()

    special_characters = ["!","$","%","^","&"]
    randLine = random.choice(lines)
    print(randLine)
    password = random.choice(lines)+random.choice(special_characters)+random.choice(lines)+str(random.randint(0,100))+random.choice(lines)+random.choice(special_characters)
    secret = canvas.create_text(canvas_width/2, canvas_height * 1/2, text=password, fill="white", font=("Helvetica",15))
    
    

# Adding the Button
button1 = Button(window, text="Click Me", command = make_password)
button1.pack()

display_area = Label(window, text = "")
display_area.pack()

window.mainloop()

