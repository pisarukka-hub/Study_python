# Find the prime factorization of a number
num = int(input())
check = 1
k = 2
residue = num
res = ""
while (num != check):
    if ((residue % k) == 0):
        check *= k
        res += str(k) + " * "
        residue = residue // k
    else:
        k += 1
print(res[:-3])