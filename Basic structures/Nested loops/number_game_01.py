# Find the winner of a kindergarten competition based on the sum of digits in their number.
winnersum = 0
sum = 0
for i in range(int(input())):
    name = str(input())
    number = int(input())
    while (number != 0):
        sum += number % 10
        number //= 10
    if (sum >= winnersum):
        winnersum = sum
        winnername = name
    sum = 0
print(winnername)