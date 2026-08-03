# Left only every second digit of a number (from highest including)
n = int(input())
even = ""
odd = ""
residue = 0
if n > 100:
    while (n > 100):
        residue = n % 100
        even = str(residue // 10) + even
        odd = str(residue % 10) + odd
        n = n // 100
    if n > 10:
        res = str(n // 10) + even
    else:
        res = str(n % 10) + odd
else:
    if n > 10:
        res = str(n // 10) + even
    else:
        res = str(n % 10) + odd
print(res)