# Calculate the greatest common divisor of two numbers using the Euclidean algorithm
a = int(input())
b = int(input())
if (a < b):
    a, b = b, a
while b:
    a, b = b, a % b
print(a)
