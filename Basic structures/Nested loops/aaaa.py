
numbers_of_lines = int(input())
line_length = int(input())
column_length = 0
i = numbers_of_lines * line_length
while (i != 0):
    column_length += 1
    i //= 10
for i in range(1, numbers_of_lines + 1):
    if (i % 2 == 0):
        for m in range(line_length):
            print(f"{(numbers_of_lines * m + i): >{column_length}}", end=" ")
        print(f"{(numbers_of_lines * (line_length)  + i): >{column_length}}")
    else:
        for m in range(line_length):
            print(f"{(numbers_of_lines * (line_length - m) + i): >{column_length}}", end=" ")
        print(f"{(numbers_of_lines * (line_length)  + i + 1): >{column_length}}")

                    