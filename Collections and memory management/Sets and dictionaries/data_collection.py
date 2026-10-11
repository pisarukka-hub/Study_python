d = []
names = []
for i in range(int(input())):
    name, preference = str(input()).split()
    d[name] += preference
for name, preference in d.items():
    if str(input()).replace(" ", "") in preference:
        names.append(name)
names.sort()
if len(names) > 0:
    print("\n".join(names))
else:
    print("Таких нет")