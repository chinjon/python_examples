name = 'John Doe'
age = 35
height = 74 # inches
weight = 180 # pounds
weight_kilograms = weight * 0.4535924
height_centimeters = height * 2.54
eyes = 'Brown'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"He's {round(height_centimeters)} cemtimeters tall.")
print(f"He's {weight} pounds heavy.")
print(f"He's {round(weight_kilograms)} kilograms heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

total = age + height + weight

print(f"If I add {age}, {height}, and {weight} I get {total}.")