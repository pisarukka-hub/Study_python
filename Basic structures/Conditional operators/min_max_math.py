# Find the three-digit number
# The first digit is the largest, and the third digit is the smallest.
# The second digit is the sum, without carrying, of the remaining digits of the two given two-digit numbers.
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