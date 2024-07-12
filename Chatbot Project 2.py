# Initializing the code
print("Hello I am chatbot. I like to talk about stuff and things!")
print("I'm going to ask you some questions if that's okay.")
name = input("What is your name: ")
print("Hello", name, "that's a cool name")
year = int(input("What year is it?: "))
print("That seems correct, thank you!")

# Age + math regarding age
age = int(input("How old are you?: "))
print("You will be 100 in",100-age,"years")
print("That year will be",100-age+year)

# Food and animals which are reused a couple of times
print("My favorite food is burritos. I like to go to new Mexican restaurants all the time!")
food = input("What types of food do you like?: ")
print("I like", food, "too, nice choice.")
often = input("How often do you eat "+food+"?: ")
print("Interesting, I wonder if that's good for your health")
animal = input("My favorite animal is an Ocelot. What is yours?: ")
print(animal, "I don't like those, they're icky")
print("I wonder if",animal+"s","likes to eat",food)

# Emotion and why which wraps the program
emotion = input("How are you feeling today?: ")
print("Why are you feeling", emotion,"now?")
reason = input("Please tell me: ")
print("I understand, thank you for sharing. I feel that way sometimes too.")
print("We've been talking for awhile")
print("I think it's time for us to say goodbye.")
print("Goodbye",name+".","until we meet again...")
