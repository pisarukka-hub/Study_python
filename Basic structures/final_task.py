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
Rating_1, Rating_2, Rating_3 = -1, -1, -1
Name_1, Name_2, Name_3 = "", "", ""
Max = 0
Min = Q + 1
Sum = 0
flag = True

if ((N >= 3) and (M > 0) and (cw > 0) and (sw > 0) and (hw > 0) and (tw > 0)):

    for student in range(N):
        student_name = str(input())
        rating = 0

        for lesson in range(M):
            a, b, c, d = map(int, input().split(","))
            rating += (a * cw) + (b * sw) + (c * hw) + (d * tw)

        if (rating > Q):
            flag = False
            break

        Sum += rating

        if rating > Rating_1:
            Rating_3, Name_3 = Rating_2, Name_2
            Rating_2, Name_2 = Rating_1, Name_1
            Rating_1, Name_1 = rating, student_name
            Max = rating

        elif rating > Rating_2:
            Rating_3, Name_3 = Rating_2, Name_2
            Rating_2, Name_2 = rating, student_name

        elif rating > Rating_3:
            Rating_3, Name_3 = rating, student_name
        if (rating < Min):
            Min = rating

else: 
    flag = False

if (flag):
    Rating_1 = round(Rating_1 / Q * 100)
    Rating_2 = round(Rating_2 / Q * 100)
    Rating_3 = round(Rating_3 / Q * 100)
    Average = round(Sum / N / Q * 100)
    Max = Rating_1
    Min = round(Min / Q * 100)

    print(Max, Average, Min)
    print(Name_1, " ", Rating_1, "%", sep="")
    print(Name_2, " ", Rating_2, "%", sep="")
    print(Name_3, " ", Rating_3, "%", sep="")

    if (Average > 50):
        print("Курс усваивается хорошо")
    else: 
        print("Курс усваивается плохо")

else:
    print("Во введённых данных ошибка")





