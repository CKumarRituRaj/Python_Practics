#Automorphic Number(a number whose square ends with the given number)
num=int(input("Enter a number "))
l=num*num
m=num
p=0
while(m>0):
    p=p+1
    m=m//10
if(num==l%(10**(p))):
    print(num," is Automorphic Number")
else:
    print(num," is not an Automorphic Number")
