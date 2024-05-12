# function to swap
def swap(string):
    start = string[0]   #statement to get the first charecter
    end = string[-1]    #statement to get the last charecter
    swapped_string = end + string[1:-1] + start #swaping last and first charecter
    print(swapped_string)#printing the swapped string

#input statement to get values from keyboard
string=input('Enter the string: ')
swap(string)#function call of swap
