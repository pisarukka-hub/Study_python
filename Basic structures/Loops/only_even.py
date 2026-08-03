res = ""
n = int(input())
while ((n != 0)):
    if ((n % 10) % 2 != 0):
        res = str(n % 10) + res
    n = n // 10
print(res)