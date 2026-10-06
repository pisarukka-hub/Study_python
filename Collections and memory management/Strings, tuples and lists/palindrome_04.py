# Check if the string is a palindrome, ignoring spaces and letter case.
s = input().lower().replace(" ", "")
if s == s[::-1]:
    print("YES")
else:
    print("NO")