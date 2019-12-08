out = False
while out == False:
    
    print ("Enter three numbers")
    a = int(input())
    b = int(input())
    c = int(input())
    print(max(a,b,c))
    choice = input ("Finish the action? (Yes/No)")
    if choice == 'Yes':
        out = True
        print('End of program')
        exit()
    elif choice == "No":
        out = False
        print('Back to the program')

