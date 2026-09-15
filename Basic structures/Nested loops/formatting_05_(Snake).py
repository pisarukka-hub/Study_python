# Showing numbers in a rectangular pattern in a zig-zag manner 

#  1  2  3  4  5  6  7
# 14 13 12 11 10  9  8
# 15 16 17 18 19 20 21
# 28 27 26 25 24 23 22
# 29 30 31 32 33 34 35
# 42 41 40 39 38 37 36

numbers_of_lines = int(input())
line_length = int(input())
column_length = 0
i = numbers_of_lines * line_length
while (i != 0):
    column_length += 1
    i //= 10
for i in range(numbers_of_lines):
    if (i % 2 == 0):
        for k in range(1, line_length):
            print(f"{(k + i * line_length): >{column_length}}", end=" ")
        print(f"{(i + 1) * line_length: >{column_length}}")
    else:
        for k in range(1, line_length):
            print(f"{((line_length + 1 - k) + i * line_length): >{column_length}}", end=" ")
        print(f"{(i * line_length + 1): >{column_length}}")

                