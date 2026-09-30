# Cut titles if they are too long
L = int(input())
for i in range(int(input())):
    head = str(input())
    if len(head) > L:
        print(head[:L - 3], end='...\n')
    else: 
        print(head)
    