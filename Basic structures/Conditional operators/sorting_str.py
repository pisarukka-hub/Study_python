# Sort three names in alphabetical order and print the first one.
name1 = str(input())
name2 = str(input())
name3 = str(input())
if (name1 < name2) and (name1 < name3):
    print(name1)
elif name2 < name3:
    print(name2)
else:
    print(name3)