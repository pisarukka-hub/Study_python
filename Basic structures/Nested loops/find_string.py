answer = 0
for i in range(int(input())):
    while ((k := str(input())) != "ВСЁ"):
        if (k == "зайка"):
            answer += 1
print(answer)
