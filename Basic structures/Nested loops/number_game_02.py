# Find the largest digit in each number and print them together
max_digit = 0
answer = ""
for i in range(int(input())):
    n = int(input())
    while (n != 0):
        digit = n % 10
        if (digit > max_digit):
            max_digit = digit
        n //= 10
    answer += str(max_digit)
    max_digit = 0
print(answer)