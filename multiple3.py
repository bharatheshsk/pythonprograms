def print_multiples_of_3():
    for i in range(3, n + 1, 3):  # Loop from 3 to N with a step of 3
        print(i, end=" ")  # Printing the value of i with a space at the end
n = int(input("Enter the value of N:"))  # user to input the value of N
# Call the function to execute
print_multiples_of_3()
