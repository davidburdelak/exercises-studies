print("###CALCULATOR###")
def addition (a,b):
    return a + b

def subtraction (a,b):
    return a - b

def multiplication (a,b):
    return a * b

def division (a,b):
    if b==0:
        print("Can't action")
    else:
        return a / b

def exponentiation (a,b):
    return a ** b

def root (a):
    import math
    return math.sqrt(a)
    
out = False
while out == False:

    a = int(input("Enter A:"))
    b = int(input("Enter B:"))

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
         print(addition(a,b))
 
    elif select == '2':
        print(subtraction(a,b))
 
    elif select == '3':
         print(multiplication(a,b))
 
    elif select == '4':
         print(division(a,b))

    elif select == '5':
         print(exponentiation(a,b))

    elif select == '6':
         print(root(a))

    else:
     print("ERROR, Select position from menu!")
