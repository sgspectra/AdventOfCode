#open input file
input = open("day3/input.txt")
#read the first line
line = input.readline()
#binary masks
pos1 = 0b000000000001
pos2 = 0b000000000010
pos3 = 0b000000000100
pos4 = 0b000000001000
pos5 = 0b000000010000
pos6 = 0b000000100000
pos7 = 0b000001000000
pos8 = 0b000010000000
pos9 = 0b000100000000
pos10 = 0b001000000000
pos11 = 0b010000000000
pos12 = 0b100000000000

gamma = 0b000000000000

pos_array = [pos1,pos2,pos3,pos4,pos5,pos6,pos7,pos8,pos9,pos10,pos11,pos12]
ones_array = [0,0,0,0,0,0,0,0,0,0,0,0]
zero_array = [0,0,0,0,0,0,0,0,0,0,0,0]

while line != "":
    byte = int(line, 2)
    ind = 0
    for x in pos_array:
        if x & byte == 0:
           zero_array[ind] += 1
        else:
            ones_array[ind] += 1
        ind += 1
    line = input.readline()

for (x,y,z) in zip(zero_array,ones_array,pos_array):
    if x < y:
        gamma = gamma | z

epsilon = gamma ^ 0b111111111111

print(epsilon * gamma)