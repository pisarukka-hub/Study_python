# Check whether the input string is a palindrome.
line = str(input())
if line == line[::-1]:
    print("YES")
else:
    print("NO")