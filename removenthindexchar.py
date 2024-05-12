#get the string and nth index value from the keyboard
s=input("Enter the String:")
n=int(input("enter the nth index value"))
print(s[:n-1]+s[n:]) #logic to remove the the Nth index
