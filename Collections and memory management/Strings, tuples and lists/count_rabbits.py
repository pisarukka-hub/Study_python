# Count how many times the word "rabbit" appears in the descriptions.
answer = 0
for i in range(int(input())):
    answer += str(input()).count("rabbit")
print(answer)
