# loads in the 'argv' module
from sys import argv
# retrieves from command line
# first argument = script name
# second argument = argv index 0
script, first, second, third = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)

# example command python ex13.py hello big world
# output:
# The script is called: ex13.py
# Your first variable is: hello
# Your second variable is: big
# Your third variable is: world