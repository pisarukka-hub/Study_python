#  Reverse Polish Notation
s = input().split()
digits = []
for ch in s:
    if ch.isdigit():
        digits.append(int(ch))
    elif ch in ["+", "-", "*", "/"]:
        if ch == "+":
            digits.append(digits.pop(-2) + digits.pop(-1))
        elif ch == "-":
            digits.append(digits.pop(-2) - digits.pop(-1))
        elif ch == "*":
            digits.append(digits.pop(-2) * digits.pop(-1))
        elif ch == "/":
            digits.append(digits.pop(-2) // digits.pop(-1))
    elif ch in ["~", "!", "#"]:
        if ch == "~":
            digits.append(-digits.pop(-1))
        elif ch == "!":
            fact = digits.pop(-1)
            for i in range(1, fact):
                fact *= i
            digits.append(fact)
        elif ch == "#":
            digits.append(digits[-1])
    elif ch == "@":
        digits[-3], digits[-2], digits[-1] = digits[-2], digits[-1], digits[-3]
print(*digits)

