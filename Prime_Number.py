flag=0
a=2
num=int(input("Enter a number = "))
if(num==0 or num==1):
        flag=1
else:
        while(a<num/2):
                if(num%a==0):
                        flag=1
                a=a+1
if(flag==0):
        print(num,"is Prime Number")
else:
        print(num,"is not Prime Number")
        
