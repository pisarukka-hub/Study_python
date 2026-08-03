# Find the largest digit in a number
num = int(input())
largest = 0
while (num > 0):
    if ((k := num % 10) > largest):
        largest = k
    num = num // 10
print(largest)