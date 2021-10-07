# Change name for each file
input_filename = "input_file.txt"

# Open pipe for input file
input_file = open(input_filename, 'r')

# create output file
output_filename = "output_file.txt"
output_file = open(output_filename, 'w')

# number of desired lines 
number_of_head_lines = 2
number_of_tail_lines = 2

## HEAD LINES ##

# create array of lines
head_lines = []
for current_line in range(number_of_head_lines):
    head_lines.append(input_file.readline())

# store last line in var: last_line
tail_lines = []

# reopening to ensure integrity of file
with open(input_filename) as file:
         
    # read last number_of_tail_lines lines from back of file
    for line in (file.readlines() [-number_of_tail_lines:]):
        tail_lines.append(line)

# write head_tail to output file
head_tail = [head_lines, tail_lines]
for each in range(len(head_tail)):
    output_file.writelines(head_tail[each])

# close pipes
input_file.close()
output_file.close()

# console output
print("Done. Copied a total of " + str(number_of_head_lines) + " head lines and " + str(number_of_tail_lines) + " tail lines: \n \n")
for each in head_lines:
    print(each)
print("-"*30)
for each in tail_lines:
    print(each)
