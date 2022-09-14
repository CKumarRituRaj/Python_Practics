#Spy Number (the sum of all the digits is equal to the product of all digits)
num=int(input("Enter a number "))
b=num
c=0
d=1
while(b>0):
    p=b%10
    c=c+p
    d=d*p
    b=b//10
if(d==c):
    print(num,"is spy number")
else:
    print(num,"is not a spy number")