a = float(input())
b = float(input())
c = float(input())
k = 0.0
m = 0.0
if (a != 0):
    D = b * b - 4 * a * c
    if D < 0:
        print("No solution")
    else:
        k = float((- b + (D ** 0.5)) / 2 / a)
        m = float((- b - (D ** 0.5)) / 2 / a)
        if k > m:
            print(f"{m:.2f} {k:.2f}")
        elif m > k:
            print(f"{k:.2f} {m:.2f}")
        else:
            print(f"{k:.2f}")
else:
    if b == 0:
        if c == 0:
            print("Infinite solutions")
        else:
            print("No solution")
    else:
        x = - c / b
        print(f"{x:.2f}") 
