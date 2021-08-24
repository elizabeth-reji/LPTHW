from sys import exit
from random import random

def get_choice(valid_inputs):
    nice_list = "[" + ", ".join(valid_inputs) + "]"

    while True:
        choice = input(f"Choices are {nice_list}\n> ")
        choice = choice.strip()

        is_choice_valid = False
        for valid in valid_inputs:
            if choice == valid:
                is_choice_valid = True

        if is_choice_valid:
            return choice
        else:
            print("Invalid choice")

def trap_door():
    print("aaaaaaaa!!!!!!!!!!!!😱")
    print("you fall into a pit filled with snakes and scorpions!!!🐍🦂")
    dead()


def gold_room():
    print("This is the final door of the game.")
    print("As you open the door you enter into a room full of gold.")
    print("Wherever you look there is gold everywhere!!!!🤩")
    print("Now comes the best part.....!!")
    print("As a reward you can take gold with you.")
    print("Well how much do you take...???")

    choice = input("> ")

    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead("Man, learn to type a number.")

    if how_much < 100:
        print("""
        Nice, you're not greedy, you win!🎊
        🎊🎊🥳🥳🎊🎊🤩🤩🎊🎊
        """)
        exit()
    else:
        dead("You greedy bastard!")


def room_dragon():
    print("You enter the room and see a dragon.")
    print("It starts to spit fire at you.")
    print("What do you do?")

    choice = get_choice(["give water", "fight"])

    if choice == "give water":
        print("you realize that the dragon had something spicy 🥵 hence he was spitting fire.")
        print("So you give him bubble tea🧋 which he takes.")
        print("after drinking it the dragon becomes bubbly and lets you go.✨🐉✨")
        print("You see two doors in front of you.")
        print("Which one do you take the left or the right one?")

        choice = get_choice(["left", "right"])

        if choice == "left":
            trap_door()
        if choice == "right":
            print("Congratulations!!!!! YOU HAVE FINALLY REACHED THE LAST STAGE")
            gold_room()

    if choice == "fight":
        print("The dragon becomes angry and picks you up.🐲🔥")
        print("He starts to roast you like a chicken🍗🍖 and eats you for his dinner")
        print("Well that was tasty!")
        dead()

def how_do_you_walk():
    choice = get_choice(["silently", "just walk directly"])

    if choice == "silently":
        print("The baby doesn't wake up..you are safe🤫.")
        print("which door do you choose?")

        choice = get_choice(["right", "left"])
        if choice == "right":
            trap_door()
        if choice =="left":
            print("Congratulations!!!!! YOU HAVE FINALLY REACHED THE LAST STAGE")
            gold_room()

    elif choice == "just walk directly":
        print("OH NO!!! the baby wakes up")
        print("It starts crying!!!")
        print("The baby picks you up and starts hitting you towards the wall.")
        print("☠️")
        dead()

def do_you_sing_well():
    return random() <= 0.3

def room_giant_baby():
    print("You enter the room to find a giant baby crying.")
    print("Well its a baby but its as big as the room👶🏻")
    print("The baby is crying non stop, what do you do??")

    choice = get_choice(["sing a lullaby", "bottle of milk"])

    if choice == "bottle of milk":
        print("You a give bottle of milk to the baby.")
        print("It starts drinking and eventually falls asleep.")
        print("You see two doors behind the sleeping baby.")
        print("do you go silently or just walk past the baby?")

        how_do_you_walk()

    elif choice == "sing a lullaby":
        good_singer = do_you_sing_well()
        if good_singer:
            print("You sing a lullaby to the baby.")
            print("Well seems like you are a good singer.")
            print("It puts the baby right back to sleep.")
            print("you see two doors behind the sleeping baby.")
            print("Do you go silently or just walk past the baby?")

            how_do_you_walk()
        else:
            print("You sing a lullaby to the baby.")
            print("OH MY GOD!!!!! You are such a horrible singer.")
            print("OH NO the baby wakes up.")
            print("It smashes you against the wall.")
            print("You should improve your singing skills!")
            exit()


def room_grizzlybear():
    print("As you enter this room you see a giant grizzly bear.")
    print("He looks very grumpy 😠.")
    print("Behind the bear you see a door.")
    print("To enter the next room you need to move the bear.")
    print("What do you do?")

    choice = get_choice(["honey", "fight", "exit"])

    if choice == "honey":
       print("The bear becomes happy and starts eating it.")
       print("The bear moves.")
       print("You take the opportunity to sneak around the bear.")
       print("You see two doors one to your left and one straight ahead.")
       print("What do you choose?")

       choice = get_choice(["left", "straight"])

       if choice == "left":
           fire_pit()
       if choice == "straight":
           print("You open the door and find stairs that lead you to another door.")
           room_dragon()

    elif choice == "fight":
       print("The bear gets angry.")
       print("It shreds you into pieces☠️.")
       print("oops! better luck next time!!")
       exit()
    else:
       print("Exiting")


def fire_pit():
    print("You open the door and you realize its a trap.")
    print("Before you could do anything you fall into the fire pit.")
    dead()

def does_cerebus_get_hit():
    return random() <= 0.3

def room_cerberus():
    print("You enter the room to find a huge dog with three heads.")
    print("As soon as it sees you it starts barking.")
    print("What do you do?")

    choice = get_choice(["stick", "bone","exit"])

    if choice == "stick":
        print("You take out a stick and throw it in the other direction.")
        print("Looking at the stick cereberus becomes exicited and starts wagging his tail.")
        print("He runs behind the stick and you are safe.")
        print("Now you can see two doors in front of you.")
        print("One to your right and one straight ahead.")
        print("Which one do you choose?")

        choice = get_choice(["right", "straight"])

        if choice == "right":
              fire_pit()
        if choice == "straight":
            print("You open the door and find stairs that lead you to another door.")
            room_giant_baby()
    elif choice == "bone":
        hits = does_cerebus_get_hit()
        if hits:
            print("You throw the bone at cereberus and it hits his eye.")
            print("oh no he is angry😤")
            print("He eats you instead💀")
            dead()
        else:
            print("You take out a bone and throw it at cerberus.")
            print("He becomes happy and goes to a coner to eat it.")
            print("You are safe and you see two doors one to your right and one straight ahead.")
            print("What do you choose?")

            choice = get_choice(["right", "straight"])

            if choice == "right":
               fire_pit()
            if choice == "straight":
               print("You open the door and find stairs that lead you to another door.")
               room_giant_baby()


def dead():
    print("Maybe next time try to make better decisions🤔.")
    exit()


def start():
    print("Welcome to the CASTLE OF DOOM!!!!!!")
    print("You enter a big castle.")
    print("You see a big hall with four pillars on each corner.")
    print("On the other end of the hall you see two doors.")
    print("One on your left and an other one to your right.")
    print("What do you choose?")

    choice = get_choice(["left", "right"])

    if choice == "left":
        room_cerberus()

    if choice == "right":
        room_grizzlybear()


start()
