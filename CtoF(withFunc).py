def convertor(c):# define and creating a function named as convertor
    return(9/5*c+32)#returning the value to the calling function

c=int(input("enter the value in centigrade:"))#input the value of centigrade
print("The value in farenheit is:",convertor(c))#display the of farenheit from called funtion
