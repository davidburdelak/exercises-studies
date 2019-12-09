"""
Task: Please extend the script from task 1_2. so that options appear in the calculator

5 - Power 
6 - Root

Before displaying the menu, the program should ask for two numbers (data). Then displays the menu and selection of options. Depending on the option selected, he should now apply the appropriate arithmetic operation to the numbers given at the beginning (data) and display the result.

Perform arithmetic operations using the functions learned.

Use the if statement to protect yourself from dividing by zero.
"""
print("###CALCULATOR###")
def addition (number_a,number_b):
    return number_a + number_b

def subtraction (a,b):
    return number_a - number_b

def multiplication (number_a,number_b):
    return number_a * number_b

def division (number_a,number_b):
    if b==0:
        print("Can't action")
    else:
        return number_a / number_b

def exponentiation (number_a,number_b):
    return number_a ** number_b

def root (number_a):
    import math
    return math.sqrt(number_a)
    
out = False
while out == False:

    number_a = int(input("Enter number A:"))
    number_b = int(input("Enter number B:"))

    print("###Menu###")
    print("1 - Addition")
    print("2 - Subtraction")
    print("3 - Multiplication")
    print("4 - Division")
    print("5 - Exponentiation")
    print("6 - Root")
    print("0 - Exit")

    select = input("Select position from menu: ")
    if select == '0':
        choice = input("You wanna leave the program? (Yes/No): ")
        if choice == 'Yes':
            out = True
            print('End of program!')
            exit()
        elif choice == 'No':
            out = False
            print('Back to the program')
            select = input("Select position from menu")    
 
    if select == '1':
         print(addition(number_a,number_b))
 
    elif select == '2':
        print(subtraction(number_a,number_b))
 
    elif select == '3':
         print(multiplication(number_a,number_b))
 
    elif select == '4':
         print(division(number_a,number_b))

    elif select == '5':
         print(exponentiation(number_a,number_b))

    elif select == '6':
         print(root(number_a))

    else:
     print("ERROR, Select position from menu!")
