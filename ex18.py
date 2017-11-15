def print_two(*args):
  arg1, arg2 = args
  print (f"arg1: {arg1}, arg2: {arg2}")
  
# ok, that (*args) part was pointless
# we can do it differently

def print_two_again(arg1, arg2):
  print(f"arg1: {arg1}, arg2: {arg2}")

# this just takes one argument
def print_one(arg1):
  print(f"arg1: {arg1}")
  
# no arguments for this one
def print_none():
  print("I got nothing")
  
print_two("Vorname", "Nachname")
print_two_again("Otto", "Normal")
print_one("Hello World!")
print_none()