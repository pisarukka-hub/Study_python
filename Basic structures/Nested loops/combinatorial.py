# Find all combinations of three numbers that sum up to a given total. 
# The number is at least 1
total = int(input())
print("А Б В")
for a in range(1, total - 1):
    for b in range(1, total - a):
        c = total - a - b
        print(a, b, c)