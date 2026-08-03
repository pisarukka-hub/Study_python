# Calculate the least common multiple of two numbers using the Euclidean algorithm
a = int(input())
b = int(input())
lcm = a * b
if (a < b):
    a, b = b, a
while b:
    a, b = b, a % b
lcm //= a
print(lcm)

