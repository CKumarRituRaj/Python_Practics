num=int(input("Enter a number = "))
if (num == 0):
    print("0")
 
msb = 0
num = int(num / 2)
 
while (num > 0):
    num = int(num / 2)
    msb += 1
 
print(1 << msb)
