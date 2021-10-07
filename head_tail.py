# Change name for each file
input_filename = "input_file.txt"

# create output file
output_filename = "output_file.txt"
output_file = open(output_filename,'w')

# number of desired lines 
number_of_head_lines = 3
number_of_tail_lines = 1

# create array of lines
first_lines = []
for current_line in range(number_of_head_lines):
    first_lines.append(input_file.readline())

# store last line in var: last_line
last_lines = []

# Open pipe for input file
with open(input_filename) as file:
         
    # read last number_of_tail_lines lines from back of file
    for line in (file.readlines() [-number_of_tail_lines:]):
        last_lines.append(line)

# write head_tail to output file
head_tail = [first_lines, last_lines]
for each in range(len(head_tail)):
    output_file.writelines(head_tail[each])

# close pipes
input_file.close()
output_file.close()

# console output
print("Done. Copied a total of " + str(number_of_head_lines) + " head lines and " + str(number_of_tail_lines) + " tail lines: \n \n")
for each in first_lines:
    print(each)
print("-"*30)
for each in last_lines:
    print(each)
