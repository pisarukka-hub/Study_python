# Sum of digits of a number
numb = int(input())
summ = 0
while (numb > 0):
    summ += (numb % 10)
    numb = numb // 10
print(summ)