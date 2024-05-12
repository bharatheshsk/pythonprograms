def simpleIntrest(p,n,r):# function for SI
    return ((p*n*r)/100)# formula

a=int(input("enter the principle amount"))#get input for principle amount
b=int(input("enter the num days"))#get input for time
i=int(input("enter the intrest"))#get input for rate of interest
print(simpleIntrest(a,b,i)) # print the SI
