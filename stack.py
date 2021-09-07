stack = []

while True:
    choice = input("> ")
    if choice == "exit":
        exit()

    choice = choice.split()

    if choice[0] == "push":
        if len(choice) != 2:
            print("invaild input")
        else:
            stack.insert(0,choice[1])

    elif choice[0] == "show":
        for i in range(len(stack)):
            print(f"| {stack[i]} |")
        print("-----")

    elif choice[0] == "pop":

        if len(stack) == 0:
            print("No more numbers to pop")
        else:
            print(stack.pop(0))
    else:
        print("invalid inputs")
