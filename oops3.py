## Overriding methods and super() Keyword

class Animal():

    def __init__(self,name):
        self.name = name

    def introduce(self):
        print(f"Hello my name is {self.name}")

class Dog(Animal):

    def introduce(self):
        super().introduce()  ## We use the parent method as well as the child class method information
        print("I am a Dog")

dog = Dog("Bruno") 
dog.introduce()

cat = Animal("Stacy")
cat.introduce()

class Animal():
    def __init__(self,name):
        self.name = name

    def introduce(self):
        print(f"Hello my name is {self.name}")

class Dog(Animal):
    def __init__(self,name,breed):
        super().__init__(name)
        self.breed = breed

    def introduce(self):
        print(f"Hello my name is {self.name} and i am a {self.breed}")

dog = Dog("Bruno","Labrador")      # Hello my name is Bruno and i am a Labrador
dog.introduce()           

cat = Animal("Stacy")              # Hello my name is Stacy
cat.introduce() 

