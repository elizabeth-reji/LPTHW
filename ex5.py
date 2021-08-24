name = "Elizabeth Reji"
age = 23 # not a lie
height = 65 # inches
weight = 152 # lbs
eyes = 'Brown'
teeth = 'White'
hair = 'Black'

height_in_cms = round(height * 2.54)
weight_in_kg = weight * 0.45
print(f"Let's talk about {name}.")
print(f"She's {height} inches or {height_in_cms} cms tall.")
print(f"She's {weight} pounds or {weight_in_kg} kg heavy.")
print("Actually that's not too Heavy.")
print(f"She's got {eyes} eyes and {hair} hair.")
print(f"Her teeth are usually {teeth} depending on the coffee")

# this line is tricky try to get it exactly right
total = age + height + weight
print (f"If I add {age}, {height}, {weight} I get a {total}.")
