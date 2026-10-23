class Person:
    def __init__(self,name):
        self.name = name

    def introduce(self):
        print(f"My name is {self.name}")

class Student(Person):
    def __init__(self,name,marks):
        super().__init__(name)
        self.__marks = marks

    def get_average(self):
        if not self.__marks:
            return 0        
        sum=0
        for mark in self.__marks:
            sum+= mark
        return  (sum / len(self.__marks))

    def introduce(self):
        print(self.name)
        print(self.get_average())

class Classroom():
    def __init__(self):
        self.students = []

    def add_student(self,student):
        self.students.append(student)

    def show_students(self):
        for stud in self.students:
            stud.introduce()


classroom = Classroom()

s1 = Student("Arun", [80, 90, 70])                        
s2 = Student("Maya", [60, 75, 85])

classroom.add_student(s1)
classroom.add_student(s2)

classroom.show_students()

# Output:

# Arun
# 80.0
# Maya
# 73.33333333333333