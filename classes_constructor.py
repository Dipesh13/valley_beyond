students = []
class Student:
    """immediately add student name and id as soon as we create an object of the class."""
    def __init__(self,name,student_id):
        student = {"name":name,
                   "student_id":student_id}
        students.append(student)

bob = Student("bob",1)
print(students)

foo = Student("foo",2)
print(students)