#Strong Number (number is equal to sum of factor of each digit)
num=int(input("enter a number"))
num1=num
p=1
k=0
while(num>0):
    a=int(num%10)
    while a>0:
        p=p*a
        a=a-1
    k=k+p
    p=1
    num=num//10
   
if(num1==k):
    print(k," is Strong number")
else:
    print(k," is Not Strong number")
