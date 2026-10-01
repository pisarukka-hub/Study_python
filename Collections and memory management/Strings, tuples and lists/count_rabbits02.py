# Find the position of the word "rabbit" in each line.
for i in range(int(input())):
    answer = str(input()).find("rabbit") + 1
    if answer > 0: 
        print(answer)
    else:
        print("There are no rabbits")