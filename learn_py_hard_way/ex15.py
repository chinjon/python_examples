from sys import argv 

# arguments:
  # script name
  # path to file
script, filename = argv

# open file name
txt = open(filename)

# prints out the value of the filename argument
print(f"Here's you file {filename}:")
# reads file contents
print(txt.read())
# close out file
txt.close()

# prints out the string "Type the filename again:"
print("Type the filename again:")
# program waits for input
file_again = input("> ")

txt_again = open(file_again)

# reads file
print(txt_again.read())
# close out file
txt_again.close()