num=int(input("Enter a number = "))
n=int(input("Enter bit position = "))
if((num >> n) & 1 ==1):
    print("Least Significant Bit of ",num," = 1")
else:
    print("Least Significant Bit of ",num," = 0")
