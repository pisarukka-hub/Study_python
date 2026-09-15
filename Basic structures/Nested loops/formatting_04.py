# Showing numbers in a rectangular pattern in a column-wise manner

#  1  6 11 16 21 26 31
#  2  7 12 17 22 27 32
#  3  8 13 18 23 28 33
#  4  9 14 19 24 29 34
#  5 10 15 20 25 30 35

numbers_of_lines = int(input())
line_length = int(input())
column_length = 0
i = numbers_of_lines * line_length
while (i != 0):
    column_length += 1
    i //= 10
for i in range(1, numbers_of_lines + 1):
    for m in range(line_length - 1):
        print(f"{(numbers_of_lines * m + i): >{column_length}}", end=" ")
    print(f"{(numbers_of_lines * (line_length - 1)  + i): >{column_length}}")

                