#input the value
a=int(input("enter a number"))
b=int(input("enter a number"))
c=int(input("enter a number"))
d=int(input("enter a number"))

def greatest(a,b,c,d): #function 
    if(a>b and a>c and a>d):  #check if a is greater than b,c,d
        return a#if yes then A is greater
    elif(b>a and b>c and b>d):#if no then check if B is greater than c,d
        return b #if yes then B is greater
    elif(c>a and c>b and c>d): #if no then check if C is greater than D
        return c #if yes then C is greater
    else:
        return d #D is greater

print("greatest of 4 numbers is={}".format(greatest(a,b,c,d))) #display the value
