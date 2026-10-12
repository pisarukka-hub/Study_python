# Make a dictionary with names and preferences, 
# then search for names that match a given preference.
d = {}
names = []
for i in range(int(input())):
    input_data = str(input()).split()
    name = input_data[0]
    preference = str(" ".join(input_data[1:]))
    d[name] = preference

search = str(input())

for name, preference in d.items():
    if search in preference:
        names.append(name)
        
names.sort()
if len(names) > 0:
    print("\n".join(names))
else:
    print("Таких нет")