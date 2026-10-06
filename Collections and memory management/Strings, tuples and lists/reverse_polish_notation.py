#  Reverse Polish Notation
s = input().split()
digits = []
for ch in s:
    if ch.isdigit():
        digits.append(int(ch))
    elif ch in ["+", "-", "*"]:
        if ch == "+":
            digits.append(digits.pop(-2) + digits.pop(-1))
        elif ch == "-":
            digits.append(digits.pop(-2) - digits.pop(-1))
        elif ch == "*":
            digits.append(digits.pop(-2) * digits.pop(-1))
print(*digits)
