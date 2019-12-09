"""
Task: Create the script indicating the largest number of 3 entered by the user. Perform the task in a loop so that it is possible to perform the fun until the user is asked Do finish the action and choose y / Y (yes).
"""

out = False
while out == False:
    
    print ("Enter three numbers")
    number_a = int(input())
    number_b = int(input())
    number_c = int(input())
    print(max(number_a,number_b,number_c))
    choice = input ("Finish the action? (Yes/No)")
    if choice == 'Yes':
        out = True
        print('End of program')
        exit()
    elif choice == "No":
        out = False
        print('Back to the program')
