import numpy as np
s,t,u,v,w,x,y,z=0,0,0,0,0,0,0,0
A=np.array([[1,2,3],[4,5,6],[7,8,9]])
for i in range(len(A)):
    for j in range(len(A[0])):
        if(i==j):
            s=s+A[i][j];
        if(i+j==2):
            t=t+A[i][j];
        if(i==0):
            u=u+A[i][j];
        if(i==1):
            v=v+A[i][j]; 
        if(i==2):
            w=w+A[i][j];  
        if(j==0):
            x=x+A[i][j];
        if(j==1):
            y=y+A[i][j]; 
        if(j==2):
            z=z+A[i][j];
      
print("Sum of left diognal = ",s);
print("Sum of right diognal = ",t);
print("Sum of first row = ",u);
print("Sum of second row = ",v);
print("Sum of third row = ",w);
print("Sum of first column = ",x);
print("Sum of second column = ",y);
print("Sum of third column = ",z);
