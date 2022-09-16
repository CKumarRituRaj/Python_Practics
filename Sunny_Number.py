#Sunny Number(if the number next to the given number is a perfect square)
import math
num=int(input("Enter a number "))
x=math.sqrt(num+1)
if(x==int(x)):
    print(num," is Sunny Number")
else:
    print(num," is not a Sunny Number")