#variables to store x,y position (both begin at 0)
x_pos = 0
y_pos = 0

#open input file and read first line
input_file = open("input.txt")
command = input_file.readline()

#while the input file is not at EOF
while command != "":
    #find the position of the space
    space_pos = command.find(" ")
    #get the direction word and the numerical value associated
    direction = command[0:space_pos]
    value = int(command[space_pos+1:])
    #using the direction extracted modify the x,y positions accordingly
    if direction == "forward":
        x_pos = x_pos + value
    elif direction == "down":
        y_pos = y_pos + value
    else:
        y_pos = y_pos - value
    #read next line
    command = input_file.readline()

#close file
input_file.close()
#print final position
print("Final X: " + str(x_pos))
print ("Final y: " + str(y_pos))
print(x_pos * y_pos)