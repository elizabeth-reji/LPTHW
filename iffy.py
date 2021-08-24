def f1(age):
    if age < 18:
        print("Have coke")
    else:
        print("Have rum")

def f2(age):
    if age < 10:
        print("Have milk")
    elif age < 18:
        print("Have coke")
    else:
        print("Have rum")

f2(9)
f2(16)
f2(18)
f2(45)
