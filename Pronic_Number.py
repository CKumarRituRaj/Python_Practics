#Pronic Number(A number which is the product of two consecutive integers)
import math
num= int(input("Enter a number "))
D=int(math.sqrt(num))
if(D*(D+1)==num):
    print(num,"is Pronic Number")
else:
    print(num,"is not Pronic Number")