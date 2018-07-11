students= []

def add_student(name,student_id):
    """
    1) if string is provided as input it should be enclosed in " "
    :param name:
    :param student_id:
    :return:
    """
    student = {
        "name" : name,
        "student_id" : student_id
    }
    students.append(student)

student_name = input("Enter name: ")
student_id = input("Enter id: ")

add_student(student_name,student_id)
print(students)