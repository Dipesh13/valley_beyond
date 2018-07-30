"""
Adding attributes to a class
After printing ozzy, it is clear that this object is a dog.
But you haven't added any attributes yet.Let's give the Dog class a name and age:
"""

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

ozzy = Dog("Ozzy", 2)

"""
To access an object's attributes in Python, you can use the dot notation.
This is done by typing the name of the object, followed by a dot and the attribute's name.
"""

print(ozzy.name)
print(ozzy.age)