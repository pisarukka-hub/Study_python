# Find the symmetric difference of two sets of names.

d = {} 
names = [] 
for i in range(int(input()) + int(input())):
    if (name := str(input())) in d:
        d[name] += 1
    else:
        d[name] = 1
for name, value in d.items():
    if value == 1:
        names.append(name)
names.sort()
if len(names) > 0:
    print("\n".join(names))
else:
    print("Таких нет")