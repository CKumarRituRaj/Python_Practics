#Multilevel_inheritance
class Grass():  
    def eat_grass(self):  
        print("Deer eat's Grass")
class Deer(Grass):  
    def eat_deer(self):  
        print("Fox eat's Deer")
class Fox(Deer):  
    def eat_fox(self):  
        print("Lion eat's Fox ")

d = Fox()  
d.eat_grass()
d.eat_deer()
d.eat_fox()
