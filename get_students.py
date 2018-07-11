# always returns the first element and exits
# def get_student(students):
#     for student in students:
#         return student
#
# data = ['a','b']
# students = get_student(data)
# print(students)

data = ['bob','bo','foo']

def get_student(students):
    student_len = []
    for student in students:
        student_len.append(len(student))
    return student_len

students = get_student(data)
print(students)