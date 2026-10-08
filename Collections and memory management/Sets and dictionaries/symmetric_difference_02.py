N = int(input())
M = int(input())
d = {}
names = []
for i in range(N + M):
    if (name := str(input())) in d:
        d[name] += 1
    else:
        d[name] = 0
for value in d.values():
    if value < 1:
        names.append(value)
names.sort()
if len(names) > 1:
    print("\n".join(names))
else:
    print("Таких нет")