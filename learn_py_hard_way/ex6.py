# assigns variable types_of_people with value of 10
types_of_people = 10
# assigns variable with string "There are 10 types of people"
x = f"There are {types_of_people} types of people."

# assigns variable binary with string "binary"
binary = 'binary'
# assigns variable do_not with string "don't"
do_not = "don't"
# assigns variable y with string "Those who know binary and those who don't"
y = f"Those who know {binary} and those who {do_not}"

# prints out value of x variable
  # "There are 10 types of people"
print(x)
# prints out value of y variable
  # "Those who know binary and those who don't"
print(y)

# prints out "I said: There are 10 types of people"
print(f"I said: {x}")
# prints out "I also said: 'Those who know binary and those who don't'"
print(f"I also said: '{y}'")

# assigns variable hilarious with value of False
hilarous = True
# assigns the variable joke_evaluation with "Isn't that joke so funny?!"
joke_evaluation = "Isn't that joke so funny?! {}"
print(joke_evaluation.format(hilarous))

w = "This is the left side of..."
e = "a string with a right side."

print(w + e)