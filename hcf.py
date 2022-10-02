num1=int(input("Enter first number "))
num2=int(input("Enter second number "))
if(num1==0 or num2==0):
    hcf =num1+num2
else:
    if(num1<num2):
        sml=num1
    else:
        sml=num2
    for i in range(1,sml+1):
        print(i)
        if((num1%i==0) and (num2%i==0)):
            hcf=i
print("HCF of ",num1," and ",num2," = ",hcf)