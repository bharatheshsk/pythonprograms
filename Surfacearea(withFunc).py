import math
r=int(input("enter radius of cylinder="))#input radius value
h=int(input("enter height of cylinder="))#input height value
r1=int(input("enter radius of cone="))#input height value
l=int(input("enter length of cone="))#input height value
def cylinder(r,h):#function to surface of cylinder 
    return (2*math.pi*r*h)

def cone(r1,l):#function to surface of cone
    return (math.pi*r*l)
print("surface area of cylinder{0:.2f}".format(cylinder(r,h)))#calling cylider function and printing return value
print("surface area of cone{0:.2f}".format(cone(r1,l)))#calling cone function and printing return value
