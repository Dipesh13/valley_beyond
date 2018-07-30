"""
Define methods in a class.
Now that you have a Dog class.
it does have a name and age which you can keep track of, but it doesn't actually do anything.
This is where instance methods come in.
"""

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print("bark bark!")

"""
The bark method can now be called using the dot notation, after instantiating a new ozzy object. 
"""

ozzy = Dog("Ozzy", 2)
# difference
ozzy.bark()
print(ozzy.bark())