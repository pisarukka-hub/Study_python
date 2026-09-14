numbers_of_lines = int(input())
line_length = int(input())
column_length = 0
i = numbers_of_lines * line_length
number = 0
while (i != 0):
    column_length += 1
    i //= 10
for l in range(1, numbers_of_lines + 1):
    for k in range(1, line_length):
        number += 1
        print(f"{(number): ^{column_length}}", end=" ")
    number += 1
    print(f"{(number): ^{column_length}}")

                