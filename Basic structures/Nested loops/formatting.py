# Formatting numbers in a triangular pattern
linesize = 0
line = ""
endline = 1
N = int(input())
for i in range(1, N + 1):
    if (i <= endline):
        line = line + str(i) + " "
    else:
        print(line[:-1])
        line = str(i) + " "
        linesize += 1
        endline = i + linesize
print(line[:-1])
