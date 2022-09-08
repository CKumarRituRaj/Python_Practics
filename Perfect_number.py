#Perfect number
num=int(input("Enter a number "))
a=1
k=0
while(a<num):
    if(num%a==0):
        k=k+a
    a=a+1
    
if(num==k):
    print(num," is Perfect Number")
else:
    print(num," is not a Perfect Number")
