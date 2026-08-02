# Find the shortest phrase that contains the word "rabbit" and its length. 
frase1 = str(input())
frase2 = str(input())
frase3 = str(input())
a = "z"
b = "z"
c = "z"
if "rabbit" in frase1:
    a = frase1
if "rabbit" in frase2:
    b = frase2
if "rabbit" in frase3:
    c = frase3
print(min(a, b, c), len(min(a, b, c)))
