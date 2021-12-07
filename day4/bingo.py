#open the input file
input_file = open("day4/input.txt")
#read the numbers from the first line into an array
called_numbers = input_file.readline()
called_number_array = [int(i) for i in called_numbers.split(',')]
#consume /n in input file
line = input_file.readline()

#function that will read five lines from the input file and create an array of rows
#input file should be open before calling and the last line read should be /n
def createRowArray(input_file):
    count = 0
    row_array = []
    #read 5 rows, create arrays of ints out of them and append them to the row_array
    while count < 5:
        read_row = input_file.readline()
        row = []
        for x in read_row.split(' '):
            if x != '':
                row.append(int(x))
        row_array.append(row)
        count += 1
    #consume /n
    last_read_line = input_file.readline()
    #return the row array
    return row_array, last_read_line

#function that will take in an array of rows and return us an array of columns
def createColFromRow(array_of_rows):
    count = 0
    col_array = []
    while count < 5:
        col = []
        for x in array_of_rows:
            col.append(x[count])
        col_array.append(col)
        count += 1
    return col_array
       
#arrays to hold the array of rows and the array of columns
#ex array_of_rows[0] will print all the rows in the first board
array_of_rows = []
array_of_columns = []

#create the arrays of rows and columns
while line != "":
    a, line = createRowArray(input_file)
    b = createColFromRow(a)
    array_of_rows.append(a)
    array_of_columns.append(b)



