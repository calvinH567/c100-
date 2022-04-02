class Student(object):
    def __init__(self,name,age,gender,grade):
        self.name=name
        self.age=age
        self.gender=gender
        self.grade=grade
    def setGrade(self,grade):
        self.grade=5
        print(self.grade)
Calvin=Student("Calvin",10,"Male",4)
print(Calvin.name)

