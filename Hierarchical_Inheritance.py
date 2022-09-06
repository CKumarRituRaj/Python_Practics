#Hierarchical_Inheritance
class Num:
    def get_Value(self):
        self.a=int(input("Enter first Number "))
        self.b=int(input("Enter Second Number "))
        
class Add(Num):
    def add_num(self):
        print("Sum of",self.a,"and",self.b," = ",self.a+self.b)
        
class Sub(Num):
    def sub_num(self):
        print("Substract of",self.a,"and",self.b," = ",self.a-self.b)
        
p=Add()
q=Sub()
print("For Addition")
q.get_Value()
print("For Substraction")
p.get_Value()
p.add_num()
q.sub_num()
