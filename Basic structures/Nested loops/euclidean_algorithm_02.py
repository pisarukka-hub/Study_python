# Calculate the greatest common divisor of n numbers using the Euclidean algorithm
n = int(input())
a = int(input())
for i in range(n - 1):
    b = int(input())
    if (a < b):
        a, b = b, a
    while b:
        a, b = b, a % b
    result = a
print(result)
