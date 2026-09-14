# How many blocks of strings contain the word "rabbit"?
flag = False
answer = 0
for i in range(n := int(input())):
    while ((k := str(input())) != "All"):
        if (k == "rabbit"):
            flag = True
    if (flag):
        answer += 1
    flag = False
print(answer)
