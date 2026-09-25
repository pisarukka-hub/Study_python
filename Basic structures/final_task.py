# Analysis of the educational program

# N (num_students) — numbers of students
# M (num_lessons) — numbers of lessons
# Q (max_rating) — max rating
# cw (classwork_coefficient) — classwork coefficient
# sw (selfwork_coefficient) — selfwork coefficient
# hw (homework_coefficient) — homework coefficient
# tw (testwork_coefficient) — testwork coefficient
# a (classwork_grade) — classwork grade
# b (selfwork_grade) — selfwork grade
# c (homework_grade) — homework grade
# d (testwork_grade) — testwork grade

# N >= 3
# M > 0 
# cw, sw, hw, tw > 0
# rating <= Q.

# input:
# N M Q cw sw hw tw
# student's name
# aᵢ,bᵢ,cᵢ,dᵢ

# output:
# Max Average Min ratings
# Name_1 Rating_1% (top-1)
# Name_2 Rating_2% (top-2)
# Name_3 Rating_3% (top-3)
# Курс усваивается хорошо/плохо

N, M, Q, cw, sw, hw, tw = map(int, input().split())
Rating_1, Rating_2, Rating_3 = 0, 0, 0
Max = 0
Min = Q
Sum = 0
flag = True
if ((N >= 3) and (M > 0) and (cw > 0) and (sw > 0) and (hw > 0) and (tw > 0)):
    for student in range(N):
        student_name = str(input())
        rating = 0
        for lesson in range(M):
            a, b, c, d = map(int, input().split(","))
            rating += (a * cw) + (b * sw) + (c * hw) + (d * tw)
        rating //= Q 
        if (rating > Q):
            flag = False
        if (rating < Min):
            Min = rating
        if (rating > Rating_3):
            if (rating > Rating_2):
                if (rating > Rating_1):
                    Max = rating
                    Rating_1 = rating
                    Name_1 = student_name
                else:
                    Rating_2 = rating
                    Name_2 = student_name
            else:
                Rating_3 = rating
                Name_3 = student_name
        Sum += rating
else: 
    flag = False
if (flag):
    Average = Sum // N
    print(Max, Average, Min)
    print(Name_1, Rating_1, "%")
    print(Name_2, Rating_2, "%")
    print(Name_3, Rating_3, "%")
    if (Average > 50):
        print("Курс усваивается хорошо")
    else: 
        print("Курс усваивается плохо")
else:
    print("Во введённых данных ошибка")





