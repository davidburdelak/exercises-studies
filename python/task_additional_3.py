print ("----------------------Multiplication table--------------------")
print(60*"-")
for y in range(1,11):
     for x in range(1,11):
          print (f" {x*y:>3} ", end="|")
     print()
     print(60*"-")
