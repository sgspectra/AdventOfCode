#open input file
input = open("input.txt")

#read the first line
line = input.readline()
byte = int(line, 2)

while line != "":
    print(byte)
    line = input.readline()
    byte = int(line, 2)