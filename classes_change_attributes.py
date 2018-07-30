class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def doginfo(self):
        print(self.age)

    def birthday(self):
        self.age +=1

ozzy = Dog("Ozzy", 2)
print(ozzy.age)
ozzy.birthday()
print(ozzy.age)