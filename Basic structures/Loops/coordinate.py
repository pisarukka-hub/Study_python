# Calculate the final coordinates after a series of movements in a 2D plane
x, y = 0, 0
while ((k := str(input()))!= "stop"):
    if (k == "north"):
        n = int(input())
        y += n
    if (k == "south"):     
        n = int(input())
        y -= n
    if (k == "east"):
        n = int(input())
        x += n
    if (k == "west"):
        n = int(input())
        x -= n
print(x, y, sep="\n")
