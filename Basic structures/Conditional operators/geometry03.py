# There is a ideal circle island
# And a dangerous zone insade the island with complex shape (scheme.png)
x = float(input())
y = float(input())
if x * x + y * y > 100:
    print("You are on the water. You can be eaten by a shark. Swim to the island as soon as possible!")
else:
    if y <= 0:
        if y >= 0.25 * ((x + 1) ** 2) - 9:
            print("Danger! Leave the zone as soon as possible!")
        else:
            print("The zone is safe. Continue your work.") 
    elif x >= 0:
        if x * x + y * y < 25:
            print("Danger! Leave the zone as soon as possible!")
        else:
            print("The zone is safe. Continue your work.")
    else:
        if y > 5:
            print("The zone is safe. Continue your work.")
        elif 3 * y < 5 * x + 35:
            print("Danger! Leave the zone as soon as possible!")
        else:
            print("The zone is safe. Continue your work.")