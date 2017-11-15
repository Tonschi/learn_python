from sys import argv

#define commandline arguments
script, input_file = argv

# print the whole file
def print_all(f):
  print(f.read())


# go to the start of the file
def rewind(f):
  f.seek(0)

# print a line from a file
# Line number +  the actual line
def print_a_line(line_count, f):
  print(line_count, f.readline())


current_file = open(input_file)

print("First let's print the whole file:\n")

print_all(current_file)

rewind(current_file)

print("Let's print three lines:")

# set current line to 1
current_line = 1

# this function calls the other function readline
# each time readline is being called, the read head moves further a line
# that's why all further commands will output line 2 and 3 of the input text file
# if the read header is being reset by using seek(0) ... 
# ... or repositioned by using seek(somenumber) it won't work like that
print_a_line(current_line, current_file)

# set current line to 2
# x += 1 is just a short way to write x = x + 1
current_line += 1
# intentionally break the neat script by repositioning the read head
current_file.seek(50)
print_a_line(current_line, current_file)

# set current line to 3
current_line += 1
# and break it again by resetting the read head again
current_file.seek(0)
print_a_line(current_line, current_file)