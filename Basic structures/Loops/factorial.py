# Calculate the factorial of a number using a loop
res = 1
for i in range(2, int(input()) + 1):
    res *= i
print(res)