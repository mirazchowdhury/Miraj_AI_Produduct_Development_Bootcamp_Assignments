class Person:
    def __init__(self,name):
        self.name = name
        print(self.name)
    def introduce(self):
        return f"{self.name} am a person"
class Student(Person):
    def __init__(self,name):
        self.name = name
        print("Override ",self.name)
    def introduce(self):
        return f"{self.name} am a student"
    
name = Student("Aziz")
print(name.introduce())
