# Find the three-digit number
# First digit is the largest, and third digit is the smallest. 
# Second digit is the sum without carrying of rest of the digits of the two given two-digit numbers
first = int(input())
second = int(input())
a = first // 10
b = first % 10
c = second // 10
d = second % 10
one = max(a, b, c, d)
three = min(a, b, c, d)
two = (a + b + c + d - one - three) % 10
print(one, two, three, sep="")