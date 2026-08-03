n = int(input())
m = 1
k = 2
i = n
res = ""
while (n != m):
    if ((i % k) == 0):
        m *= k
        res += str(k) + " * "
        i = i // k
    else:
        k += 1
print(res[:-3])