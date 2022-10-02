import math
a=int(input("Enter value of a ="))
b=int(input("Enter value of b ="))
c=int(input("Enter value of c ="))
d=b*b-4*a*c
if(d>0):
    k=(-b+math.sqrt(d))/2*a
    l=(-b-math.sqrt(d))/2*a
    print("First root = ",k,"\nSecond root = ",l)
elif(d==0):
    print("Root = ",-b/2*a)
else:
    print("No real roots")
