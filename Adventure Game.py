from time import sleep
death = False
visits = 0
inv = []
fullinv = ["a","b","c","d","e","f","g","h"]

print("Welcome to the Museum!")
sleep(.5)
print("You may have realized that you took a wrong turn back there.")
sleep(1)
print("Don't worry, you have just entered the INTERACTIVE wing of the museum.")
sleep(1)
print("What does interactive mean you say?")
sleep(.5)
print("...")
sleep(1)
print("Oh it means that you make choices and then those choices affect your immediate surroundings.")
print("It's completely safe...")
sleep(1)
print("I promise...")

while True:
    print("Anyways! Your first choice is about what item you want to take with you!")
    print("(A) Flashlight (B) Knife (C) Pair of Gloves (D) Bottle of Water")
    sleep(1)
    item = input("A/B/C/D: ").lower()
    inv.append(item)

    sleep(1)
    print("Maybe not what I would've picked, but okay!")
    print("Now, where would you like to visit! You can't leave until you visit at least one exhibit!")
    while True:
        print("(A) Egypt circa 2000 BC (B) Italy circa 44 BC (C) Indonesia circa 38000 BC (D) Florida 1969")
        destination = input("A/B/C/D: ").lower()
        if destination in ["a","b","c","d"]:
            print("That's an...interesting choice!")
            break
        else:
            print("Invalid entry! Try again...")

    if destination == "a":
        visits += 1
        print("You chose to go to Egypt!")
        print("Welcome to the year 2000 BC!")
        print("If you look to your left, you may notice some sand.")
        print("If you look to your right, you may notice some more sand.")
        print("If you look forward or backward, you might see some more...sand.")
        print("Let's go for a walk and see what we can see!")
        print("You want to go left or right?")
        direction = input("L/R: ").lower()
        if direction == "l":
            print("Okay, let's head in that direction!")
            print("It's been about an hour in the desert now. It's pretty hot out.")
            print("You notice that your guide has deserted you.")
            if "d" in inv:
                print("Do you want to drink some water?")
                water = input("Yes/No: ").lower()
                if water == "yes":
                    print("You quench your thirst and your guide returns.")
                    print("Hey there person, I think we've been here for long enough. You want to go home?")
                    leave = input("Yes/No: ").lower()
                    if leave == "yes":
                        print("Sounds good to me, I hate the sand anyways") 
                        continue
                    elif leave == "no":
                        print("Okay then. I guess I'll just check on you in awhile...")
                        print("The pyramids were in the other direction dummy.")
                        sleep(1)
                        print("You start walking the other direction")
                        sleep(1)
                        print("Or did you actually turn around?")
                        sleep(1)
                        print("Where am I?")
                        sleep(1)
                        print("...")
                        print("You lose")
                        death = True
                        break
                elif water == "no":
                    print("You think you see an island in the distance.")
                    print("You walk toward it, knowing that it must be salvation from this desert")
                    print("No matter how far you walk, it moves ever further away.")
                    print("You drink your water, hoping to reach this paradise")
                    print("You don't make it...")
                    death = True
                    break
        elif direction == "r":
            print("That way sounds good I suppose.")
            print("The two of you walk for awhile and before you know it you see a massive pyramid loom above you.")
            print("You can see that there are hundreds of people working.")
            print("Your guide tells you, 'Don't worry about the language, I will automatically translate for you!")
            print("Do you want to visit (A) the market or (B) the pyramid?")
            choice = input("A/B: ").lower()
            if choice == "a":
                print("You visit the market.")
            elif choice == "b":
                print("You visit the pyramid.")
                print("Do you want to (A) talk to the workers or (B) sneak into the pyramid")
                choice = input("A/B: ").lower()
                if choice == "a":
                    print("You decide to talk to the workers")
                    print("You go up to one of the workers and try to strike up a conversation")
                    print("They are initially annoyed with you, but notice that you're holding something in your hand which you immediately offer to them.")
                    if "d" in inv or "c" in inv:
                        print("Thank you for that, I think that will be very useful")
                        print("You decide to ask about their life and what they like to do")
                        print("He tells you that he is a farmer, but his land is currently flooded.")
                        print("The pharaoh sent a messenger to everyone in his village, asking if they wanted to work on this project.")
                        print("He agreed and that's why he's here.")
                        print("He continues that many people choose to work on the pyramids for the same sorts of reasons")
                        print("Your guide reappears to take you home")
                        continue
                    else:
                        print("I don't want that garbage, get out of here!")
                        print("He calls the guard over and you're locked in prison forever")
                        death = True
                        break
                elif choice == "b":
                    print("You decide to sneak into the pyramid")
                    if "a" in inv:
                        print("You run down the darkest corridor of the pyramid and find the tomb of the pharaoh")
                        print("There are riches and jewels scattered everywhere on the floor")
                        print("Your guide appears telling you it's time to go.")
                        print("Do you want to (A) Take nothing (B) Grab a small trinket (C) Grab a huge golden mask")
                        choice = input("A/B/C: ").lower()
                        if choice == "a":
                            print("You leave with your pockets empty, but you survive.")
                        elif choice == "b":
                            inv.append("e")
                            print("You leave with a small golden scarab")
                        elif choice == "c":
                            print("You try to grab a huge mask that's way too heavy to move.")
                            print("Your guide laughs at you and leaves you to the guards' mercy")
                            death = True
                    else:
                        print("It's way too dark, the guards catch you and kill you")
                        death = True
                        break


    elif destination == "b":
        visits += 1
        print("You chose to go to Italy!")
        print("You look around and immediately notice that you're in some sort of meeting.")
        print("By the looks of it...everyone looks very important.")
        print("You initially hang back a little bit to scope it out.")
        print("A senator comes up to you and says, 'You ready to do this?'")
        choice = input("Yes/No: ").lower()
        if choice == "yes" and "b" in inv:
            print("Great, a Dictator for Life is a bridge too far.")
            print("Dictator for life...Italy...")
            print("Now it makes sense, you're at the Ides of March, Caesar's assassination.")
            print("Julius Caesar is in the room next door and you're about to bust in there.")
            print("You walk in and see him discussing something with a small group of senators.")
            print("You wait a few minutes for the room to fill and then it's time.")
            print("Seeing no other option for escape, you join the group and attack Caesar.")
            print("Before the end, Caesar falls forward into your arms.")
            print("Et tu Brutus?")
            print("You grab the brooch that holds his toga in place as he falls to the ground")
            print("Your guide quickly takes you away, ")
            inv.append("f")
            continue
        elif choice == "yes":
            print("Let's do this.")
            print("You walk into the room and suddenly see a face that looks familiar.")
            print("Julius Caesar is standing among a small group of senators discussing something important.")
            print("You realize what's about to happen...the Ides of March, Caesar's assassination.")
            print("You thankfully realize that you don't have a weapon and therefore can't partcipate.")
            print("Caesar calls out for you to come to his defense")
            print("The crowd turns on you next.")
            death = True
            break
        elif choice == "no":
            print("You're a coward, Brutus.")
            print("You try to explain that this plan backfires and that Caesar's nephew takes over following Caesar's death.")
            print("It's no use and the senator get's angry.")
            print("You've been stabbed by your co-conspirator.")
            death = True
            break
    
    elif destination == "c":
        visits += 1
        print("You chose to go to Indonesia!")
        print("Your at the entrance to what appears to be a small cave.")
        print("You think you hear what sounds like people moving around inside.")
        print("Do you want to (A) go inside or (B) explore outside")
        choice = input("A/B: ").lower()
        if choice == "a":
            print("You decide to go in the cave.")
            print("You see a group of early humans huddled around a fire")
            print("Your guide is unable to fully translate, but they do their best.")
            print("You look around at the fire and see shimmering along the wall some cave paintings.")
            print("When you look at the paintings, the beings start to get agitated.")
            print("They don't like you touching the paintings and start moving towards you.")
            print("Do you want to (A) Leave the cave or (B) Go deeper into the cave")
            choice = input("A/B: ").lower()
            if choice == "a":
                print("You decide to leave the cave. The beings don't follow you.")
                print("Your guide decides to take you back to the museum empty-handed.")
            elif choice == "b":
                print("You go deeper into the cave to try and escape.")
                print("It's getting darker and darker as you progress. Soon you can't see the light from the fire in the cave.")
                print("The voices grow distant until you can no longer hear them as well")
                if "a" in inv:
                    print("Thankfully you have your flashlight.")
                    print("You turn it on and see what looks like a primitive tool left on the ground")
                    print("You pick it up and take it with you before you walk towards the now illuminated exit.")
                    print("Your guide takes you home after you escape the cave")
                    inv.append("g")
        elif choice == "b":
            print("You decide to explore the exterior grasslands")
            print("You explore around a bit and don't see very much.")
            print("There are some sparsely populated trees and grasslands, but it's very cold.")
            print("You walk for some more time and see some berries growing on a bush.")
            print("Do you want to eat the berries?")
            choice = input("Yes/No: ").lower()
            if choice == "yes":
                print("You eat the berries and die of poison.")
                death = True
                break
            elif choice == "no":
                print("You decide to not eat the berries and continue on.")
                print("As you continue, you get the distinct feeling that you're not alone out here.")
                print("Some of the smaller animals that you heard rustling in the brush when you started are no longer around")
                print("Something is off...")
                print("You see something that looks like a deer alone about 50 feet from you emerge from behind a tree")
                print("Do you want to (A) Hide or (B) Continue")
                choice = input("A/B: ").lower()
                if choice == "a":
                    print("You decide to hide even though you only see the deer.")
                    print("Thank goodness you do as out of nowhere you see a large cat jump out and attack the deer.")
                    print("Your guide pipes in saying that they think it was a Scimitar Cat, a cousin of the Sabertooth.")
                    print("With that, your guide thinks you've had enough and takes you back to the museum.")
                    continue
                elif choice == "b":
                    print("You walk up, aiming to pet the deer.")
                    print("It's actually quite a sweet moment.")
                    print("The deer, nuzzles it's mouth up to you and makes an approving snort.")
                    print("However, that doesn't stop the large cat from jumping out and attacking you.")
                    print("You die instantly to what you somehow know is a Scimitar Cat.")
                    print("The deer gallops away as the cat protects its kill from other predators.")
                    death = True
                    break
    elif destination == "d":
        visits += 1
        print("You chose to go to Florida!")
        print("Your guide chimes in...really? Florida?")
        print("Anywhere in history and you choose Florida?")
        print("That being said, you look around and realize that you're at the Space Shuttle launch heading to the Moon.")
        print("You take a moment and appreciate what exactly is going on here before someone comes up to you.")
        print("Come on Buzz, it's time to board the shuttle. Launch is coming up soon!")
        print("You try to argue, but they think it's some sort of joke.")
        print("You board the shuttle and get ready for take off.")
        print("Just as they're about to launch the shuttle, Neil Armstrong looks at you funny and gestures towards his hands.")
        print("You look down and notice you have nothing on your hands even though the rest of your suit fits great.")
        print("The prep crew must have assumed you had your gloves on the shuttle already")
        if "c" in inv:
            print("You manage to slip on the gloves you grabbed from before and get ready for takeoff.")
            print("The shuttle launches and Neil notices that something is very off with you.")
            print("He shoves you to the side and takes over on the controls that you were supposed to man along with his own.")
            print("Eventually you land on the moon")
            print("You disembark and grab a moonstone for later")
            print("After you grab the stone, your guide teleports you back to the museum.")
            inv.append("h")
            continue
        elif "c" not in inv:
            print("You don't have any gloves and eventually the pressure differential isn't good and has disastrous consequences.")
            death = True
            break        
    

    print("You've survived your visit! Do you want to visit anywhere else?")
    choice = input("Yes/No: ").lower()
    if choice == "yes":
        continue
    else:
        break

print("That appears to be the end of your stay. Hope it worked out for you!")
print("You managed to successfully visit",visits,"historical events!")
if visits == 0:
    print("Nice job genius!")
elif visits == 1:
    print("Maybe be a bit more ambitious next time.")
elif visits < 4:
    print("You were so close! You could've gone to all of the places!")
elif visits == 4:
    print("You did it!")
if death == True:
    print("It is a shame that you didn't successfully make it back though...")
elif death == False:
    print("We hope you visit again sometime!")

if set(fullinv).issubset(inv):
    print("You also found all the secret items!")