num=int(input("Enter First number = "))
num1=int(input("Enter Second number = "))
num2=int(input("Enter Third number = "))

if(num>num1):
    if(num>num2):
        print(num,"is Greatest Number")
    else:
        print(num2,"is Greatest Number")

elif(num1>num2):
    print(num1,"is Greatest Number")
else:
    print(num2,"is Greatest Number")
