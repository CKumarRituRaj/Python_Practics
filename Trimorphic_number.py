#Trimorphic number(if its cube ends in the same digits as the number itself)
num= int(input("Enter a number "))
a=num
count=0
while(a>0):
    count+=1
    a=a//10
a=num**3
a=(a%(10**count))
if(num==a):
    print(num,"is Trimorphic number")
else:
    print(num,"is not Trimorphic number")