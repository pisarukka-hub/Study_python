# show a multiplication table for n numbers with frames

#  1 | 2 | 3 
# ------------
#  2 | 4 | 6 
# ------------
#  3 | 6 | 9 
# ------------

n = int(input())
size = int(input())
line = ""
for i in range(1, n + 1):
    for j in range(1, n + 1):
        line = line + f"{(i * j): ^{size}}" + "|"
    print(line[:-1])
    if (i < n):
        print("-" * ((size + 1) * n - 1 ))
    line = ""