testword = 'hello'
vowelcounter = 0;

for x in testword:
  if x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u':
    vowelcounter += 1
    
print('Number of vowels: ' + str(vowelcounter))
