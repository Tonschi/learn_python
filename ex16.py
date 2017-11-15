# import arguments module
from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL+C.")
print("If you want that, hit RETURN.")

input("?")

print("Opening the file ...")

# open file in write mode and truncate it's contents automatically
target = open(filename, "w")

print("Truncating the file. Goodbye!")
# empty the file. erase it's contents.
#target.truncate()

print("Now I'm going to ask you for three lines.")
# ask the user to type in a few lines worth of input
line1, line2, line3 = input("line 1: "), input("line 2: "), input("line 3: ")

print("I'm going to write these to the file.")

# write te lines into the file
target.write(line1 + "\n" + line2 + "\n" + line3 + "\n")

print("And finally, we close it.")
# close the file again
target.close()