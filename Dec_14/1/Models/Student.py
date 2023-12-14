from Models.Person import Person

class Student(Person):
    def __init__(self, name: str, major: str):
        super().__init__(name)
        self.major = major

    def log(self):
        print("学生:", self.name)
        print("专业:", self.major)
        pass
