"""An example of a class is the class Dog.
Don't think of it as a specific dog, or your own dog.
We're describing what a dog is and can do, in general.

Dogs usually have a name and age; these are instance attributes.
Dogs can also bark; this is a method.

When you talk about a specific dog, you would have an object in programming:
an object is an instantiation of a class.
So my dog Ozzy, for example, belongs to the class Dog.
His attributes are name = 'Ozzy' and age = '2'.
A different dog will have different attributes.

Inside the class, an __init__ method has to be defined with def.
This is the initializer that you can later use to instantiate objects.
It's similar to a constructor in Java.

Note: self in Python is equivalent to this in C++ or Java
"""

class Dog:
    def __init__(self):
        pass


"""
Instantiating objects
To instantiate an object, type the class name, followed by two brackets.
You can assign this to a variable to keep track of the object.
"""

ozzy = Dog()
print(ozzy)