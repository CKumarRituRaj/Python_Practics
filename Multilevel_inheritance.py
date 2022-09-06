#Multilevel_inheritance
class Dog():  
    def bark(self):  
        print("dog bark")
class Cat():  
    def meow(self):  
        print("Cat Meow")
class Lion():  
    def roar(self):  
        print("Lion Roar")
class Animal(Dog,Cat,Lion):  
    def speak(self):  
        print("Animal Speaking")

d = Animal()  
d.bark()  
d.meow()
d.roar()
d.speak()
