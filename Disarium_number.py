#Disarium number(if sum of its digits powered with their respective positions is equal to the number itself)
num=int(input("Enter a Number "))
a=num
b=num
k=0
p=0
while(b>0):
    p+=1
    b=b//10

while(a>0):
    b=a%10
    k=k+(b**p)
    p-=1
    a=a//10
if(k==num):
    print(num,"is Disarium number")
else:
    print(num,"is not Disarium number")