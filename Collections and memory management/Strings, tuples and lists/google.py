# Create google
# Find lines that contain the search string, ignoring case.
base = [] 
for n in range(int(input())):
    base.append(str(input()))
search = str(input())
# Check each line for the search string
for i in base:
    if str.lower(search) in str.lower(i):
        print(i)
