# Count consecutive occurrences of each character in the string.
line = str(input())
letter = line[0]
count = 0
rln = []
for letters in line:
    if letters == letter:
        count += 1
    else:
        rln.append(letter)
        rln.append(count)
        letter = letters
        count = 1
rln.append(letter)
rln.append(count)
for i in range(1, len(rln), 2):
    print(rln[i - 1], rln[i])
    