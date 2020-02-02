
low = 0 
high = 100
correct = False
guess = 0
userIndicator = ''
print('Please think of a number between 0 and 100!')

while True:
  answer = (high+low)//2
  print('Is your secret number ' + str(answer) + '?')
  userIndicator = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
  
  if userIndicator == 'h':
    high = answer
  elif userIndicator == 'l':
    low = answer
  elif userIndicator =='c':
    break
  else:
    print('Sorry, I did not understand your input.')

print('Game over. Your secret number was: ' + str((high+low)//2))
