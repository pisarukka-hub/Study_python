# The elf, gnome, and human have the same number on same position of their two-digit numbers 
# Find common digit
elfs = int(input())
gnoms = int(input())
people = int(input())
a1 = elfs // 10
b1 = elfs % 10
a2 = gnoms // 10
b2 = gnoms % 10
a3 = people // 10
b3 = people % 10
if a1 == a2 and a1 == a3:
    print(a1)
else:
    print(b1)