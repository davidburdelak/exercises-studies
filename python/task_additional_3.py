"""
Task: Make a multiplication table from 1 to 10. Using a loop, write numbers 1 to 10 vertically and horizontally. At the intersection, enter the multiplication result.
"""

print ("----------------------Multiplication table--------------------")
print(60*"-")
for y in range(1,11):
     for x in range(1,11):
          print (f" {x*y:>3} ", end="|")
     print()
     print(60*"-")
