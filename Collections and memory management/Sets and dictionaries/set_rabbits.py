# Save all unique objects in a set
objects = set()
for i in range(int(input())):
    objects = objects | set(str(input()).split(" "))
print("\n".join(objects))
