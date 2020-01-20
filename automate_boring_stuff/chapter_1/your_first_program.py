# This program says hello and asks for my name.

print('Hello world!')
print('What is your name?')
myName = input()  # inpu asks for name
print('It is good to mee you, ' + myName)
print('The length of your name is:')
print(len(myName))  # prints out length of name from input
print('What is your age?')
myAge = input()  # asks for age
print('You will be ' + str(int(myAge) + 1) + ' in a year.')  # prints out age next year