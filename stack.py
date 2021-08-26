stack = []
while True:
    choice = input("> ")
    if choice == "exit":
        exit()

    choice = choice.split()
    #print(choice)
    if choice[0] == "push":
        stack.insert(0,choice[1])
    elif choice[0] == "show":
        print(stack)








#while <condition>:
#    statement 1
#    statment 2
#    print(adada)
#    input(adad)
