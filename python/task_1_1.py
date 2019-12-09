"""
Task: Please write a script that displays the menu of the following form:

*******************CALCULATOR******************
1 - Addition
2 - Subtraction
3 - Multiplication
4 - Division
0 - End

It will then prompt you which option to choose, print the selected option number, and exit.
"""
#DEVELOPED BY DAVID BURDELAK
print ("*******************CALCULATOR*******************")

def menu():
    print ("1 - Addition")
    print ("2 - Subtraction"),
    print ("3 - Multiplication")
    print ("4 - Division")
    print ("0 - End")
menu()
operation = input("What you pick ?")
if operation=="1": print ("Choice: addition")
elif operation=="2": print ("Choice: subtraction")
elif operation=="3": print ("Choice: multiplication")
elif operation=="4": print ("Choice: division")
elif operation=="0": print ("Choice: You leave")
