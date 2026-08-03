# Count the number of strings containing the word "rabbit"
with_rabbit = 0
for i in range(int(input())):
    if ("rabbit" in str(input())):
        with_rabbit += 1
print(with_rabbit)