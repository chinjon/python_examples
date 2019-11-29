from sys import argv

# arguments
# script = script name
# filename = path of file
script, filename = argv

# prints out "We're going to erase __filename__"
print(f"We're going to erase {filename}.")
# prints out "If you don't want that, hit CTRL-C"
print("If you don't want that, hit CTRL-C (^C).")
# prints out "If you do want that, hit RETURN"
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
# assigns the variable with the open function with filename
# 'w' flag opens the file and truncates it first
target = open(filename, 'w')

print("Truncating the file. Goodbye!")
# truncate command is unecessary 
# target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

target.write(line1 + "\n" + line2 + "\n" + line3 + "\n")

print("And finally, we close it.")
target.close()