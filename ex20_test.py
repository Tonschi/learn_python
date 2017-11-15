from sys import argv

# define input arguments for our script
script, input_file = argv

textfile = open(input_file)

print(textfile.readline())
textfile.seek(0)
print(textfile.readline())
print(textfile.readline())