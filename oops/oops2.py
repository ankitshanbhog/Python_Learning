
## Basic Inheritance ##

class Person:
    def __init__(self,name):
        self.name = name

    def introduce(self):
        print( f"Hello My name is {self.name}")


class Student(Person):
    def submit_assignment(self):
        print(f"{self.name} submitted an assignment")


student = Student("Ankit")

student.submit_assignment()

