num = int(input())    
find_digit = num
digit = 0.1
is_palindrome = True
while (find_digit > 0):
    find_digit = find_digit // 10
    digit *= 10
while (digit > 1):
    if ((num // digit) != (num % 10)):
        is_palindrome = False
        print("NO")
        break
    num = (num % digit) // 10
    digit = digit // 100
if is_palindrome:
    print("YES")