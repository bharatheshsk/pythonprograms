def print_values_of_n():
    n = int(input("Enter the value of N:"))  #user to input the value of N
    for i in range(1, n + 1):  # Loop from 1 to N 
        print(i, end=" ")  # Printing the value of i with a space at the end
# Call the function to execute
print_values_of_n()
