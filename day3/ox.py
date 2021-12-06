#open the input file
input_file = open("day3/input.txt")
#get the first line of the input
line = input_file.readline()
input_array = []
#put all of the lines from the input file into an array
while line != "":
    input_array.append(line)
    line = input_file.readline()
#close input file
input_file.close()

def tallyAndRemove(array, pos):
    kept_elements = []
    #go through the input file and tally weather there are more ones or zeroes in position 1
    zero_count = 0
    one_count = 0
    for x in array:
        character = x[pos]
        if character == "1":
            one_count += 1
        else:
            zero_count += 1
    #using the counts, remove the data points that do not meet the specification
    if zero_count > one_count:
        for x in array:
            if x[pos] == '0':
                kept_elements.append(x)
    else:
        for x in array:
            if x[pos] == '1':
                kept_elements.append(x)

    #clear out the old input array and replace it with just the elements kept
    return kept_elements

print(len(input_array))

count = 0
while count < 12:
    input_array = tallyAndRemove(input_array, count)
    count += 1

print(len(input_array))
print(int(input_array[0], 2))

