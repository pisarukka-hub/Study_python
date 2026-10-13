# Count the numuber of people with the same surname
list_of_names = {}
count = 0
for n in range(int(input())):
    name = str(input())
    if name in list_of_names:
        list_of_names[name] += 1
    else:
        list_of_names[name] = 1
for name, value in list_of_names.items():
    if value > 1:
        count += value
print(count)
