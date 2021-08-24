from sys import argv

# read the WYSS section for how to run this
script, first, second, third = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)


"""

argv = ["ex13.py", "apple", "bada-apple", "chotta-apple"]
script, first, second, third = argv

script = "ex13.py"
first = "apple"



argv = [ "ex13.py", "first", "2nd", "3rd" ]

        script,      first,   second, third, = argv


script = "ex13.py"
first = "first"
second = "2nd"
third = "3rd"
"""
