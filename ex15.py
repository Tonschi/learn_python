# import arguments module
from sys import argv

# define some arguments
script, filename = argv

# open the file as requested by the commandline
txt = open(filename)

# print the file to the commandline and close it again
print(f"Here's your file {filename}:")
print(txt.read())
txt.close()

# now let the user type in a filename to open
print("Type the filename again:")
file_again = input("> ")

# open that file
txt_again = open(file_again)

# print the file contents to the shell
print(txt_again.read())
txt_again.close()