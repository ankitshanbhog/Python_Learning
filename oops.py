class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def calculate_average(self):
        if not self.marks:
            return 0.0

        return (sum(self.marks) / len(self.marks))


student1 = Student("Max",[99,98,100])

print(student1.calculate_average())

