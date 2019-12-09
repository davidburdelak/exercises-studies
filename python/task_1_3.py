"""
Extend the script from task 1_2 so that option 5 - Factorial appears in the calculator and the program uses the recursive loop to calculate the factorial from the given number. Add option 6 - Power and 7 - Root.
"""
#DEVELOPED BY DAWID BURDELAK
import math

print("##### CALCULATOR #####")
 
out = False
while out == False:
 
    print("##### Menu ######")
    print("1 - Addition")
    print("2 - Subtraction")
    print("3 - Multiplication")
    print("4 - Division")
    print("5 - Factorial")
    print("6 - Power")
    print("7 - Root")
    print("0 - Exit")
 
    choice = input("Select an action: ")
 
    if (choice == '0'):
        question = input("Exit the program? (Yes/No): ")
        if (question == 'Yes'):
            out = True
            print('End the program')
            exit()
        elif (question == 'No'):
            out = False
            print('Back to the program')
            choice = input("Select an action:")
 
    if (choice == '1'):
        print('Your choice is addition.')
 
    elif (choice == '2'):
        print('Your choice is subtraction.')
 
    elif (choice == '3'):
        print('Your choice is multiplication.')
 
    elif (choice == '4'):
        print('Your choice is division.')

    elif (choice == '5'):
        print('Your choice is factorial.')

        factorial = 1
        try:
            n = int(input("Enter a number: "))
            result = 1
            for i in range(1,n+1):
                result = result*i
            print("Result: ")
            print(result)
        except ValueError:
            print("Error, enter a number.")
        
    elif (choice == '6'):
        print('Your choice is power.')

        try:
            number = float(input("Enter a number: "))
            print("Result: " + str(number**2))
        except ValueError:
            print("Error, enter a number.")

    elif (choice == '7'):
        print('Your choice is root')

        try:
            number = float(input("Enter a number: "))
            print("Result: " + str(math.sqrt(number)))
        except ValueError:
            print("Error, enter a number.")

    else:
         print("ERROR")
