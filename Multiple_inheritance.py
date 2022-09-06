#Multiple_inheritance
class Addition(): 
    def get_add(self):
        self.a=int(input("Enter first number "))
        self.b=int(input("Enter second number "))
    def add(self):  
        print("Sum of ",self.a," and ",self.b," = ",self.a+self.b)
class Substraction():  
    def get_sub(self):
        self.c=int(input("Enter first number "))
        self.d=int(input("Enter second number "))
    def sub(self):  
        print("Substract of ",self.c," and ",self.d," = ",self.c-self.d)
class Solution(Addition,Substraction):  
    def solve(self):  
        print("Solution ")

d = Solution()
d.solve()
print("For Addition ")
d.get_add()  
print("For Substraction ")
d.get_sub()
d.add()
d.sub()
