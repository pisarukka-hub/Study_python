# Is the triangle acute, right, or obtuse?
a = float(input())
b = float(input())
c = float(input())
m = max(a, b, c)   # longest side
s = a * a + b * b + c * c - m * m   # sum of other sides
if m * m < s:
    print("acute")
elif m * m == s:
    print("right")
else:
    print("obtuse")