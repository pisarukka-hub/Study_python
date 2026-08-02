# A beautiful number is a three-digit number in which 
# the sum of the largest and smallest digits is equal to twice the middle digit. 
# Check if the given number is beautiful.
number = int(input())
a = number // 100
b = (number // 10) % 10
c = number % 10
big = max(a, b, c)
small = min(a, b, c) 
if (big + small) == ((a + b + c - big - small) * 2):
    print("YES")
else:
    print("NO")