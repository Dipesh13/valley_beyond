students= []

def add_student(name,student_id):
    student = {
        "name" : name,
        "student_id" : student_id
    }
    students.append(student)

def save_file(student):
    try :
        f = open("students.txt","a")
        f.write(student+'\n')
        f.close()
    except Exception as e:
        print(e)


def read_file():
    try:
        f = open("students.txt",'r')
        for student in f.readlines():
            add_student(student)
        f.close()
    except Exception as e:
        print("file not found")

read_file()
print(students)

student_name = input("Enter name: ")
student_id = input("Enter id: ")

add_student(student_name,student_id)
save_file(student_name)

read_file()
print(students)