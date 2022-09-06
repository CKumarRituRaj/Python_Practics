a=1
num=int(input("Enter your number = "))
while(num>0):
    #print(num%2," ")
    a=a*10+num%2
    num=num//2

while(a>10):
    print(int(a%10))
    a=a/10
