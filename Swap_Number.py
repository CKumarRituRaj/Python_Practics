num =int(input("Enter first number = "))
num1 =int(input("Enter Second number = "))
print("Before Swap First Number = ",num)
print("Before Swap Second Number = ",num1)
num^=num1
num1^=num
num^=num1
print("After Swap First Number = ",num)
print("After Swap Second Number = ",num1)
