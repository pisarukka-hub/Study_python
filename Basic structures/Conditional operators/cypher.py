# New password is ragging of two sums of digits of the old password.
# The first sum is the sum of the last two digits, and the second sum is the sum of the first two digits.
# Print the larger sum first, then the smaller one.
password = int(input())
a = password // 100
b = (password // 10) % 10
c = password % 10
sum1 = b + c 
sum2 = a + b
if sum1 > sum2:
    print(sum1, sum2, sep="")
else:
    print(sum2, sum1, sep="")