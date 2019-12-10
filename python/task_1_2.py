"""
Task: Extend the script from task 1 so that the program does not end after the selected option is implemented, but starts processing from the beginning (from the menu display, the data remains the same!). The script should end after selecting option 0 (look at menu).
Additionally, protect the menu from choosing other options than the range from 0-4.
Tip: put the whole (almost) script inside the while loop, the condition of which will be that the option is different (! =) from zero.
"""
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
