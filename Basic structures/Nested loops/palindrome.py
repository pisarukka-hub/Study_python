# Count how many palindromes is from n numbers 
count = 0
for i in range(int(input())):
    number = int(input())
    number_str = str(number)
    palindrome = ""
    while (number != 0):
        palindrome += str(number % 10)
        number //= 10
    if (palindrome == number_str):
        count += 1
print(count)