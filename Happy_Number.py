#Happy Number(a happy number is a number which eventually reaches 1 when replaced by the sum of the square of each digit.)
sum=0
num=int(input("Enter a number"))
while(sum!=1 and sum!=4):
    sum=0
    while(num>0):
        temp=num%10
        sum=sum+(temp*temp)
        num=num//10
    num=sum

if(sum==1):
    print("Happy Number")
else:
    print("UnHappy Number")