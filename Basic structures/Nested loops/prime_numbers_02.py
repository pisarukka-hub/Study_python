# Count the number of prime numbers in a given list of numbers
answer = 0
for i in range(int(input())):
    n = int(input())
    divisors = 0
    for j in range(1, n + 1):
        if (n % j == 0):
            divisors += 1
    if (divisors == 2):
        answer += 1
print(answer)