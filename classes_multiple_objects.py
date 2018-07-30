class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def doginfo(self):
        """
        self.name etc are variables which can be accessed from all methods inside a class
        :return:
        """
        print(self.name + " is " + str(self.age) + " year(s) old.")

ozzy = Dog("Ozzy", 2)
skippy = Dog("Skippy", 12)

ozzy.doginfo()
skippy.doginfo()