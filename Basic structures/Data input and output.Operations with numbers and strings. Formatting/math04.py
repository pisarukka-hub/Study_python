# A car travels from point A to point B at a speed of C km/h. 
# Find how many hours it will take to travel the distance between points A and B.
A = int(input())
B = int(input())
C = int(input())
distance = abs(A - B)
time = distance / C
print(f"{time:.2f}")