# Formatting numbers in a triangular pattern

#    1    
#   2 3   
#  4 5 6  
# 7 8 9 10
#  11 12  

number = int(input())
line = ""
number_of_longest_line = 0
rest_of_numbers = number

while (rest_of_numbers >= number_of_longest_line):
    rest_of_numbers -= number_of_longest_line
    number_of_longest_line += 1
last_line_size = 0

for i in range(number - rest_of_numbers + 1, number + 1):
    last_line_size += len(str(i)) + 1
last_line_size -= 1
penul_line_size = 0

for i in range(number - rest_of_numbers - number_of_longest_line + 2, number - rest_of_numbers + 1):
    penul_line_size += len(str(i)) + 1
penul_line_size -= 1

if (last_line_size > penul_line_size):
    line_size = last_line_size
else: 
    line_size = penul_line_size
this_line_size = 0

line = ""
endline = 1
for i in range(1, number + 1):
    if (i <= endline):
        line = line + str(i) + " "
    else:
        print(f"{line[:-1]: ^{line_size}}")
        line = str(i) + " "
        this_line_size += 1
        endline = i + this_line_size
print(f"{line[:-1]: ^{line_size}}")
