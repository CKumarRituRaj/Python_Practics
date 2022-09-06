num =int(input("Enter Year = "))
if(num%400==0):
    print(num,"is Prime Number")
elif(num%100==0):
    print(num,"is not Prime Number")
elif(num%4==0):
    print(num,"is Prime Number")
else:
    print(num,"is not Prime Number")
