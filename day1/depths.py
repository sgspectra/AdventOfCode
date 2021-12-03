input_file = open("day1/input.txt")
#get the first value from the list
previous_value = input_file.readline()
#get the next value in the list
next_value = input_file.readline()
#variable to store number of larger values
larger_count = 0
#while not at EOF compare the two values and add to tally if larger
while next_value != "":
    if int(next_value) > int(previous_value):
        larger_count += 1
    previous_value = next_value
    next_value = input_file.readline()
#close file
input_file.close()
#print the amount of values that are larger
print(larger_count)
