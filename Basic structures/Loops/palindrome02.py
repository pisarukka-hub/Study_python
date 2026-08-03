num = int(input())
N = num
palindrome = 0
while (num > 0):
    palindrome = (palindrome * 10) + (num % 10)
    num = num // 10
    print(palindrome)
if (palindrome == N):
    print("YES")
else:
    print("NO")