# Raise each number to the given power.
numbers = list(map(int, input().split()))
power = int(input())
for i in range(len(numbers)):
    numbers[i] **= power
print(*numbers)