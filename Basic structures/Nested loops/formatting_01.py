# Formatting numbers in a triangular pattern

# 1
# 2 3
# 4 5 6
# 7 8 9 10

linesize = 0
line = ""
endline = 1
for i in range(1, int(input()) + 1):
    if (i <= endline):
        line = line + str(i) + " "
    else:
        print(line[:-1])
        line = str(i) + " "
        linesize += 1
        endline = i + linesize
print(line[:-1])
