# Find the number system with biggest sum of digits

number = int(input())
answer = 0
summ = 0
maxsumm = -1
for i in range(2, 11):
    n = number
    summ = 0
    while (n > 0):
        base = 1
        while (n >= base * i):
            base *= i
        summ += n // base
        n %= base
    if summ > maxsumm :
        answer = i
        maxsumm = summ
    summ = 0
print(answer)