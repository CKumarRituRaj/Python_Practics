#Single_Inheritance
class Student:
    def getdeta(self):
        self.roll=int(input("Enter your roll no "))
        self.name=input("Enter Your Name ")
    def showdata(self):
        print("Name = ",self.name)
        print("Roll = ",self.roll)

class Exam(Student):
    def getsub(self):
        self.sub1=input("Enter your first Subject ")
        self.sub2=input("Enter your second Subject ")
    def showsub(self):
        print("First Subject = ",self.sub1)
        print("Second Subject = ",self.sub2)

        
d=Exam()
d.getdeta()
d.getsub()
d.showdata()
d.showsub()
