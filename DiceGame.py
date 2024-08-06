import random
import time
win = ""
loss = ""
tie = ""
def roll_dice(n,s):
    dice = []
    for i in range(n):
        dice.append(random.randint(1,s))
    return dice
def find_winner(user,computer):
    global win, loss, tie
    computer_total = sum(computer)
    user_total = sum(user)
    print("User Total:",user_total)
    print("Computer Total:",computer_total)
    if user_total == computer_total:
        tie=True
        return tie
    elif user_total > computer_total:
        win=True
        return win
    elif computer_total > user_total:
        loss=True
        return loss
def roll_again(choices, dice_list):
    print("Rerolling based on selections...")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("...")
    time.sleep(1)
    for i in range(len(choices)):
        if choices[i] == "r":
            dice_list[i] = random.randint(1,sides)
    print(dice_list)
def computer_strategy1(n):
    print("The computer is figuring out how to beat you.")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("...")
    time.sleep(1)
    choices = ""
    for i in range(n):
        choices = choices + "r"
    return choices

def computer_strategy2(n, user, computer):
    print("The computer is figuring out how to beat you.")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("...")
    time.sleep(1)
    choices = ""
    computer_total = sum(computer)
    user_total = sum(user)
    if user_total > computer_total:
        choices=""
        for i in range(n):
            if computer_rolls[i] < sides:
                choices = choices + "r"

            else:
                choices = choices + "-"
        print(choices)
    return choices

num = int(input("How many dice do you want to roll?: "))
sides = int(input("How many sides on the dice?: "))

user_rolls = roll_dice(num,sides)
print(user_rolls)
computer_rolls = roll_dice(num,sides)
print(computer_rolls)
print("Enter - to hold or r to roll again.")
print("Example (5 dice): --rr-")
print("This would reroll the 3rd and 4th dice in the sequence.")
user_choices = input("Enter - to hold or r to roll again: ").lower()
while len(user_choices) != num:
    print("Invalid entry, you must enter", num,"choices.")
    user_choices = input("Enter - to hold or r to roll again: ")
roll_again(user_choices,user_rolls)
computer_choices = computer_strategy2(num, user_rolls, computer_rolls)

for i in range(2):
    roll_again(computer_choices,computer_rolls)
print("Player final rolls:",user_rolls)
print("Computer final rolls:",computer_rolls)

find_winner(user_rolls,computer_rolls)

if win:
    print("You Win!")
elif loss:
    print("You Lose!")
elif tie:
    print("You Tie!")