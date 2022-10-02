num1=int(input("Enter first number "))
num2=int(input("Enter second number "))
if(num1==0 or num2==0):
    lcm =0
else:
    if(num1>num2):
        grt=num1
    else:
        grt=num2
    while(1):
        if((grt%num1==0) and (grt%num2==0)):
            lcm=grt
            break
        grt+=1
print("LCM of ",num1," and ",num2," = ",lcm)