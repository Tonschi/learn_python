from sys import argv
from os.path import exists

script, from_file, to_file = argv

print("Copying from {} to {}".format(from_file, to_file))
indata = open(from_file).read()
out_file = open(to_file, "w").write(indata)