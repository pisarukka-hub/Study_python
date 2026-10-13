dic = {}
while (string := str(input())) != "":
    items = string.split()
    for item in items:
        if item in dic:
            dic[item] += 1
        else:
            dic[item] = 1
for item, count in dic.items():
    print(item, count)