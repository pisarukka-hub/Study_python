# Raise each number to the given power.
numbers = []
for n in range(int(input())):
    numbers.append(int(input()))
power = int(input())
for i in range(len(numbers)):
    print(numbers[i] ** power)