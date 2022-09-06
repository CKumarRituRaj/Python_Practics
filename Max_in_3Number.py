num =int(input("Enter first number = "))
num1 =int(input("Enter Second number = "))
num3 =int(input("Enter Third number = "))
max=num if num>num1 else num1
max1=max if max>num3 else num3
print("Maximum number of ",num,num1,"and",num3," = ",max1)
