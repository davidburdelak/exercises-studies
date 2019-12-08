#DEVELOPED BY DAWID BURDELAK
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
