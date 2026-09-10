line = ""
k = 1
N = int(input())
for i in range(1, N + 1):
    if (k <= N ):
        line = line + str(N) + " "
    else:
        print(line[:-1])
        line = ""
        k = k + N + 1