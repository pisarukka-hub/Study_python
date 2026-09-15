# Showing numbers in a rectangular pattern in a column-wise manner

#  1 10 11 20 21 30 31
#  2  9 12 19 22 29 32
#  3  8 13 18 23 28 33
#  4  7 14 17 24 27 34
#  5  6 15 16 25 26 35

numbers_of_lines = int(input())
line_length = int(input())
column_length = 0
i = numbers_of_lines * line_length

while (i != 0):
    column_length += 1
    i //= 10

for i in range(1, numbers_of_lines + 1):
    for m in range(line_length - 1):
        if (m % 2 == 0):
            print(f"{(numbers_of_lines * m + i): >{column_length}}", end=" ")
        else:
            print(f"{(numbers_of_lines * m  + (numbers_of_lines - i) + 1): >{column_length}}", end=" ")
    if (line_length % 2 != 0):
        print(f"{(numbers_of_lines * (line_length - 1)  + i ): >{column_length}}")
    else:
        print(f"{(numbers_of_lines * (line_length - 1)  + (numbers_of_lines - i) + 1): >{column_length}}")

                    