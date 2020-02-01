testString = 'azcbobobegghakl'
list = []
alpha = ''

for x, letter in enumerate(testString):
  if x+1 < len(testString):
    if letter <= testString[x+1]:
      print(letter)
      alpha += letter
      if x != 0 and letter >= testString[x-1]:
        print(letter)
        alpha += letter
    elif letter >= testString[x+1]:
      list.append(alpha)
      alpha = ''
  else:
    if letter >= testString[x-1]:
      print(letter)

print list
# enumerate through each string index
# per string
  # if current string is greater than previous but less than next
