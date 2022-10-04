if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([score, name])
  
    students_left = [student for student in students if student[0] != min(students)[0]]
    [print(student[1]) for student in sorted(students_left) if student[0] == min(students_left)[0]]