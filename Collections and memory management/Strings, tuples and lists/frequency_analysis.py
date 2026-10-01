# Find the most frequently occurring letter in the text.
letters = []
count = []
answer = []
while (row := str(input())) != "ФИНИШ":
    row = row.lower()
    for letter in row:

        if letter == " ":
            continue

        if letter not in letters:
            letters.append(letter)
            count.append(0)
        count[letters.index(letter)] += 1

max_count = max(count)

for i in range(len(letters)):
    if count[i] == max_count:
        answer.append(letters[i])
print(sorted(answer)[0])