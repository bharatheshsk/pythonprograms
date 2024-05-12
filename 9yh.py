def findLen(s):
  count = 0
  for char in s:
    count += 1
  return count

S = input("Enter a string: ")
length = findLen(S)
print("The length of the string is:", length)
