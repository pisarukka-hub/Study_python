# Find the largest and smallest two-digit numbers that can be formed from the digits of a three-digit number.
number = int(input())
a = number // 100
b = (number // 10) % 10
c = number % 10
big = max(a, b, c)
small = min(a, b, c) 
middle = a + b + c - big - small
if small != 0:
    minnum = small * 10 + middle
elif middle != 0:
    minnum = middle * 10 + small
else:
    minnum = big * 10 + middle
maxnum = big * 10 + middle 
print(minnum, maxnum)