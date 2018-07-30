"""
Passing arguments to methods
You would like for our dogs to have a buddy. This should be optional, since not all dogs are as sociable.
Take a look at the setBuddy() method below.
It takes self, as per usual, and buddy as arguments.

Set the self.buddy attribute to buddy, and the buddy.buddy attribute to self.
This means that the relationship is reciprocal; you are your buddy's buddy.

"""

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def setBuddy(self, buddy):
        self.buddy = buddy
        buddy.buddy = self

ozzy = Dog("Ozzy", 2)
filou = Dog("Filou", 8)

ozzy.setBuddy(filou)

print(ozzy.buddy.name)
print(ozzy.buddy.age)

print(filou.buddy.name)