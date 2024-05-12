# Write a program for finding surface areas of cylinder and cone (2*PI*r*h, PI*r*l) 
import math #this import statement is used to import the Math lib
#to get the values of Radius and height of cylinder
r1=int(input("Enter the Radius of the cylinder:"))
h=int(input("Enter the height of cylinder:"))
SA1=2*math.pi*r1*h#formula to calculate Surface area of Cylinder

print("The surface area of the Cylinder is:",SA1)#printing the surface area value of cylinder
#to get the values of Radius and length of cone
r2=int(input("Enter the Radius of the cone:"))
l=int(input("enter the length of the cone:"))
SA2=math.pi*r2*l#formula to calculate Surface area of cone

print("The surface area of the Cone is:",SA2)#printing the surface area value of cone

