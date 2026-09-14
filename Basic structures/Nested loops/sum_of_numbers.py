# Find sum of digits of k numbers.
sum = 0
for i in range(k := int(input())):
    n = int(input())
    while (n != 0):
        sum += n % 10
        n //= 10
print(sum)