#DEVELOPED BY DAWID BURDELAK
print("##### CALCULATOR #####")
 
out = False
while out == False:
 
    print("##### Menu ######")
    print("1 - Addition")
    print("2 - Subtraction")
    print("3 - Multiplication")
    print("4 - Division")
    print("0 - Exit")
    
 
    choice = input("Select an action:")
 
    if choice == '0':
        question = input("Exit the program? (Yes/No): ")
        if question == 'Yes':
            out = True
            print('End the program')
            exit()
        elif question == 'No':
            out = False
            print('Back to the program')
            choice = input("Select an action:")
 
    
 
    if choice == '1':
         print('Your choice is addition')
 
    elif choice == '2':
        print('Your choice is subtraction')
 
    elif choice == '3':
         print('Your choice is multiplication')
 
    elif choice == '4':
         print('Your choice is division')
 
    else:
     print("ERROR")
