#Neon number(number is equal to the sum of the digits of its square)
num=int(input("Enter a number "))
l=num
p=0
while(l>0):
    k=l%10
    p=p+k
    l=l//10
if(num==p*p):
    print(num," is Neon Number")
else:
    print(num," is not a Neon Number")
