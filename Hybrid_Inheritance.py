#Hybrid_Inheritance

class Name():
    def get_name(self):
        self.a=input("Enter Your Name ")
    def show_name(self):
        print("Name = ",self.a)
class Roll(Name):
    def get_roll(self):
        self.b=int(input("Enter Roll Number "))
    def show_roll(self):
        print("Roll = ",self.b)
class Class():
    def get_class(self):
        self.c=input("Enter your class ")
    def show_class(self):
        print("Class = ",self.c)
        
class Result(Roll,Class):
    def get_mark(self):
        self.d=int(input("Enter your marks "))
    def show_mark(self):
        print("Result = ",self.d)
        
obj = Result()
obj.get_name()
obj.get_roll()
obj.get_class()
obj.get_mark()
obj.show_name()
obj.show_class()
obj.show_roll()
obj.show_mark()
