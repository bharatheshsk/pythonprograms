#5. Find the greatest of four nos ( using and operator)   
#input the values of A,B,c,d
a=int(input("Enter the value of A:"))
b=int(input("Enter the value of B:"))
c=int(input("Enter the value of c:"))
d=int(input("Enter the value of d:"))

if(a>b and a>c and a>d): #check if a is greater than b,c,d
    print("A id greater",a)#if yes then A is greater
elif(b>c and b>d):#if no then check if B is greater than c,d
    print("B is greator:",b)#if yes then B is greater
elif(c>d):#if no then check if C is greater than D
    print("C is greater:",c)#if yes then C is greater
else:
    print("D is greater:",d)#D is greater
    
