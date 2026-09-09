# Find the first name in alphabetical order
firstname = "\u1000"
for i in range(int(input())):
    firstname = min(firstname, str(input()))
print(firstname)
