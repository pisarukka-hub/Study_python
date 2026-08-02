# Who will win the race?
# Draw the pedestals for the first, second, and third place winners.
first_speed = float(input())
first_name = 'Petya'
second_speed = float(input())
second_name = 'Vasya'
third_speed = float(input())
third_name = 'Tolya'
if first_speed < second_speed:
    first_speed, second_speed = second_speed, first_speed  # Rearranging the speeds
    first_name, second_name = second_name, first_name  # Rearranging the names
if second_speed < third_speed:
    second_speed, third_speed = third_speed, second_speed  # Rearranging the speeds
    second_name, third_name = third_name, second_name  # Rearranging the names
if first_speed < second_speed:
    first_speed, second_speed = second_speed, first_speed  # Rearranging the speeds
    first_name, second_name = second_name, first_name  # Rearranging the names
print(f"{first_name: ^24}")
print(f"{second_name: ^8}")
print(f"{third_name: >22}") 
one = "I"
two = "II"
three = "III" 
print(f"{two: ^8}{one: ^8}{three: ^8}")   
