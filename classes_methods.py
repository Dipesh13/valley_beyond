students = []

class Student:
    def add_student(self,name,student_id):
        student = {"name":name,"student_id":student_id}
        students.append(student)

student = Student()
student.add_student("Bob",1)

print(students)