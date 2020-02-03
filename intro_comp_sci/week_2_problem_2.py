biggest = ''
alpha = ''
s = 'pjxlkqnzpuxouuqgftfnq' # pux
# s = 'camuzfpytcrbod'

for x, letter in enumerate(s):
  #print('iterate', letter)
  if alpha == '':
    alpha += letter
  elif letter >= s[x-1]:
    print(letter, s[x-1])
    if x != len(s)-1:
      if letter >= s[x+1]:
        print(letter, s[x+1])
        alpha += letter
        if len(alpha) > len(biggest):
          biggest = alpha
          alpha = '' 
      else:
        alpha += letter  
    else:
      if len(alpha) > len(biggest):
        biggest = alpha
        alpha = ''
  else: 
    if len(alpha) > len(biggest):
      biggest = alpha
      alpha = ''      
      
print('Longest substring in alphabetical order is: ' + str(biggest))
