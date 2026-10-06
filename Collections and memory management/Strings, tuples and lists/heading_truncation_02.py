# Truncate headings to fit the given length.
length = int(input())
length -= 3
headings = []
for i in range(int(input())):
    headings.append(str(input()))
i = 0
k = 0
result = []
while len(headings[i]) < length - k:
        k+= len(headings[i])
        result.append(headings[i])
        i+= 1
result.append(headings[i][:length - k] + "...")
print(*result, sep='\n' )
