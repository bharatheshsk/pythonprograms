def print_values_of_n():
    n = int(input("Enter the value of N:"))  # user to input the value of N
    for i in range(0, n + 1, 2):  # Loop from 0 to N with a step of 2
        print(i, end=" ")  # Printing the value of i with a space at the end

# Call the function to execute
print_values_of_n()
