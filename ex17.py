from sys import argv
from os.path import exists

script, from_file, to_file = argv

print("Copying from {} to {}".format(from_file, to_file))

from_file = open(from_file)
indata = from_file.read()

print (f"The input file is {len(indata)} bytes long.")

print (f"Does the output file exist? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL+C to abort.")

out_file = open(to_file, "w")
out_file.write(indata)

print("Alright, all done.")

out_file.close()
from_file.close()