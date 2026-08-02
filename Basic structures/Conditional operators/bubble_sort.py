# Who will win the race?
first_speed = float(input())
first_name = 'Petya'
second_speed = float(input())
second_name = 'Vasya'
third_speed = float(input())
third_name = 'Tolya'
if first_speed < second_speed:
    first_speed, second_speed = second_speed, first_speed  # rearranging the speeds
    first_name, second_name = second_name, first_name  # rearranging the names
if second_speed < third_speed:
    second_speed, third_speed = third_speed, second_speed  # rearranging the speeds
    second_name, third_name = third_name, second_name  # rearranging the names
if first_speed < second_speed:
    first_speed, second_speed = second_speed, first_speed  # rearranging the speeds
    first_name, second_name = second_name, first_name  # rearranging the names
print("1.", first_name)
print("2.", second_name)
print("3.", third_name)    