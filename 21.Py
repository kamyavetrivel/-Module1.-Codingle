class student:
    grade=9
    name="Kamya"
    def introduction(self):
        print("Hi im a Student")
    def details(self):
        print("My name is",self.name)
        print("my Grade is",self.grade)
obj=student()
obj.introduction()
obj.details()
