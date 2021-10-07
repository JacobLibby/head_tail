# Change name for each file
input_filename = "input_file.txt"
input_file = open(input_filename, 'r')

# store first line in var: first_line
first_line = input_file.readline() 

# store last line in var: last_line
import os
with open(input_filename, 'rb') as f:
    f.seek(-2, os.SEEK_END)
    while f.read(1) != b'\n':
        f.seek(-2, os.SEEK_CUR)
    last_line = f.readline().decode()

# create output file
output_filename = "output_file.txt"
output_file = open(output_filename,'w')

# write head_tail to output file
head_tail = [first_line, last_line]
output_file.writelines(head_tail)

# close pipes
input_file.close()
output_file.close()
