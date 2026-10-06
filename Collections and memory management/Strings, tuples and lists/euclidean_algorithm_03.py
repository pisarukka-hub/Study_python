# Calculate the greatest common divisor of n numbers using the Euclidean algorithm
numbers = list(map(int, input().split()))
if len(numbers) > 1:
    a = numbers[0]
    for i in range(1, len(numbers)):
        b = numbers[i]
        if (a < b):
            a, b = b, a
        while b:
            a, b = b, a % b
        result = a
    print(result)
else:
    print(*numbers)
