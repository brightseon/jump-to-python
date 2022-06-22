marks = [90, 25, 67, 45, 80]

number = 0
for mark in marks:
    number = number + 1

    if mark >= 60:
        print('%d번 학생 합격' % number)
    else:
        print('%d번 학생 불합격' % number)
