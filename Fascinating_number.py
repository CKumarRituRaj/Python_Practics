#Fascinating number (When a number( 3 digits or more ) is multiplied by 2 and 3, and when both these products are concatenated with the original number, then it results in all digits from 1 to 9 present exactly once.)

num=int(input("Enter a three digit number "))
flag=0
count=0
z=1
while(z<=10):
    a=num
    b=num*2
    c=num*3
    while(a>0):
        p=a%10
        if(p==z):
            flag=1
        a=a//10
    while(b>0):
        p=b%10
        if(p==z):
            flag=1
        b=b//10
    while(c>0):
        p=c%10
        if(p==c):
            flag=1
        c=c//10
    z+=1
    if(flag==1):
        count+=1
    else:
        break
    flag=0
if(count==10):
    print(num,"is Fascinating number")
else:
    print(num,"is not Fascinating number")