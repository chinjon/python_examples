from sys import argv

script = argv

print("Entire filename to read:")
target = input("> ")

txt = open(target)
print(txt.read())
txt.close()

