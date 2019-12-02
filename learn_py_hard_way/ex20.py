# python3 ex20.py assets/ex16_test.txt 

# imports the argv module
from sys import argv

# defines the variables from arguments
  # script: first argument - name of script
  # input_file: second argument - path of file
script, input_file = argv

# creates function called print_all
  # takes an argument that should be a file path
  # function will read file contents and print
def print_all(f):
  print(f.read())
  
# creates a function called rewind
# the function "restarts" the readline position of the file to 0
def rewind(f):
  f.seek(0)
  
# creates a function called pint_a_line
# will iterate through each line after readline is called
def print_a_line(line_count, f):
  print(line_count, f.readline())

# assigns variable current_file with contents of file
current_file = open(input_file)

# prints out "first let's print the whole file:"
print("First let's print the whole file:\n")

# prints out variable current_file value
print_all(current_file)

# prints out "Now let's rewind, kind of like a tape"
print("Now let's rewind, kind of like a tape.")

# restarts readline position
rewind(current_file)

# prints string "Let's print three lines:"
print("Let's print three lines:")

# sets value of current_line to 1
current_line = 1
print_a_line(current_line, current_file)

# current_line = current_line + 1
current_line += 1
print_a_line(current_line, current_file)

# current_line = current_line + 1
current_line += 1
print_a_line(current_line, current_file)
