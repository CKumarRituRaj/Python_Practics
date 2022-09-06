import math
first=float(input("Enter first side of triangle = "))
second=float(input("Enter second side of triangle = "))
third=float(input("Enter third side of triangle = "))
s=(first+second+third)/2
k=s*(s-first)*(s-second)*(s-third)
print("Area of triangle = ",math.sqrt(k))
