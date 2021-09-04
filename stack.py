stack = []

while True:
    choice = input("> ")
    if choice == "exit":
        exit()
    choice = choice.split()
    if choice[0] == "push":
        stack.insert(0,choice[1])
    elif choice[0] == "show":
        for i in range(len(stack)):
            print(f"| {stack[i]} |")
        print("-----")
    elif choice[0] == "pop":
        print(stack.pop(0))
        if len(stack) == 0:
            print("No more numbers to pop")
            exit()
    else:
        print("invalid inputs")
