# Count the number of people with the same surname.
list_of_names = {}
count = 0

for n in range(int(input())):
    name = input()

    if name in list_of_names:
        list_of_names[name] += 1
        count += 1
    else:
        list_of_names[name] = 1

for name in sorted(list_of_names):
    if list_of_names[name] > 1:
        print(name, '-', list_of_names[name])

if count == 0:
    print("Однофамильцев нет")
