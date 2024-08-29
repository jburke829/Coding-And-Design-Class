import pandas as pd
from tkinter import *

# GETTING LISTS FOR COMPARISON LATER
# CSV GATHERED DATA FROM WORLD POPULATION REVIEW AND US BUREAU OF LABOR STATISTICS
# I COMPILED THEM INTO ONE FILE FOR EASE OF CODING

df = pd.read_csv(r"C:\Users\james\OneDrive\Documents\LESLEYMATERIALS\CodingAndDesign\median-income-by-country-2024 - median-income-by-country-2024.csv")
list_of_rows = [list(row) for row in df.values]
print(list_of_rows)
countries = df["Country"].tolist()
print(countries)
dollars = df["Median"].tolist()
print(dollars)

# WINDOW SETUP
root = Tk()
root.geometry("500x500")
root.title("Button Clicker")

# CREATING VARIABLES
number = 0
upgrades = 1
cost = 10
i=0

# When you click the button, update the text.
# Comparison deals with checking the list created at the beginning. If your dollars > than the next value in the list, it updates the information displayed
def ClickButton():
    global number, i 
    number+=upgrades
    ShowInfo["text"] = "You've earned " + str(number) + " dollars."
    if number >= dollars[i]:
        Comparison["text"] = "The median income of " + str(countries[i]) + " is " + str(dollars[i])
        i+=1

# Logic for increasing the strength of your click
def UpgradeClicks():
    global upgrades, number, cost
    if number >= cost:
        number -= cost
        ShowInfo["text"] = "You've earned " + str(number) + " dollars."
        upgrades += 1
        cost = int(cost*1.2)
        UpgradeButton["text"] = text=str(cost)+" to upgrade"
        INSTRUCTIONS["text"] = text="1 click = $"+str(upgrades)

# Button and Label setup, command attribute calls the functions from above
ClickingButton = Button(root, text="click me", padx=50, pady=50, bg="gold", font=("Arial, 16"), command=ClickButton)
ShowInfo = Label(root, text="You going to click something?", font=("Arial,20"), fg="green", pady=20)
Comparison = Label(root, text="Ready for some knowledge?", font=("Arial,20"), fg="red", pady=20)
UpgradeButton = Button(root, text=str(cost)+" to upgrade", padx=30, bg="blue", fg="white", font=("Arial, 18"), command=UpgradeClicks)
INSTRUCTIONS = Label(root, text="1 click = $1", font=("Arial,20"), fg="purple", pady=20)

# Initialization and running the loop
ClickingButton.pack()
ShowInfo.pack()
Comparison.pack()
UpgradeButton.pack()
INSTRUCTIONS.pack()

root.mainloop()
