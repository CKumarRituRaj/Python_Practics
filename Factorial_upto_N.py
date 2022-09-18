#Factorial upto N numbers
num= int(input("Enter a number "))
a=num
k=1
while(k<=a):
    print("Factorial of",k,"= ")
    b=k
    x=1
    while(b>0):
        x=x*b
        b-=1
    print(x,"\n")
    k+=1