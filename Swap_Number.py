num =int(input("Enter first number = "))
num1 =int(input("Enter Second number = "))
print("Before Swap First Number = ",num)
print("Before Swap Second Number = ",num1)
num^=num1
num1^=num
num^=num1

print("\nAfter first swap")
print("First Number = ",num)
print("Second Number = ",num1)
num,num1=num1,num
print("\nAfter Second swap")
print("First Number = ",num)
print("Second Number = ",num1)
num=num+num1
num1=num-num1
num=num-num1
print("\nAfter Third swap")
print("First Number = ",num)
print("Second Number = ",num1)
num=num*num1
num1=num//num1
num=num//num1
print("\nAfter Forth swap")
print("First Number = ",num)
print("Second Number = ",num1)
