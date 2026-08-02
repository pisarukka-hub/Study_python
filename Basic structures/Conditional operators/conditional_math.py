# Petya has 6 + M apples, and Vasya has N apples. Who has more apples?
N = int(input())
M = int(input())
if (6 + M - N) < 0:
    print("Petya")
else:
    print("Vasya")