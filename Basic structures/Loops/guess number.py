guess = 500
start = 1
end = 1001
while (True):
    print(guess)
    answer = str(input())
    if (answer == "correct"):
        break
    elif (answer == "lower"):
        end = guess
        guess = (start + end) // 2
    elif (answer == "higher"):
        start = guess
        guess = (start + end) // 2
    


