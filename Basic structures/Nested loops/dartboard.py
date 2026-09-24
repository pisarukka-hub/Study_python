# Show the numbers in rectangle pattern

# 1 1 1 1 1
# 1 2 2 2 1
# 1 2 3 2 1
# 1 2 2 2 1
# 1 1 1 1 1

N = int(input())
line = ""
column_size = len(str((N + 1)//2))
for row in range(1, N + 1):
    for col in range(1, N + 1):
        number = min(row, col, N - row + 1, N - col + 1)
        line += f"{str(number): >{column_size}}" + " "
    print(line[:-1])
    line = ""
