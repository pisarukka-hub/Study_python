n = int(input())
m = 0
while (n != m):
    for i in range(2, n + 1):
        if (n % i == 0):
            n = n // i
            m *= i
            print(i, sep=" * ", end="")
        print(i)
    