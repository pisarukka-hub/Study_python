# Check if a number is prime
prime_number = True
num = int(input())
if (num == 1):
    print("NO")
else:
    for i in range(2, ((num // 2) + 1)):
        if ((num % i) == 0):
            print("NO")
            prime_number = False
            break
    if prime_number:
        print("YES")
    
