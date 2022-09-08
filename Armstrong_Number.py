#Armstrong number(Number is equal to sum of each digit of power(number of digit))
num=int(input("enter a number"))
num1=num2=num
p=1
k=0
count=0
while(num>0):
    num=num//10
    count+=1
   
while(num2>0):
    a=int(num2%10)
    co=count
    while(count>0):
        p=p*a
        count=count-1
    k=k+p
    p=1
    count=co
    num2=num2//10
   
if(num1==k):
    print(num1," is Armstrong number")
else:
    print(num1," is Not Armstrong number")
