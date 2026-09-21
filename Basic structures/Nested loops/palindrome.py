#Count how many palindromes is from n numbers
for i in range(int(input())):
    count = 0
    number = int(input())
    number_str = str(number)
    palindrome = ""
    while (number != 0):
        palindrome += str(number % 10)
        number //= 10
    if (palindrome == number_str):
        count += 1
    print(number_str)
    print(palindrome)
    print(count)    
    palindrome = ""
print(count)