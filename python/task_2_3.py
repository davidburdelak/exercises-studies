import math

numberA = int(input('Enter a: '))
numberB = int(input('Enter b: '))
numberC = int(input('Enter c: '))
if (numberA!=0):
    delta=(numberB*numberB)-(4*numberA*numberC)
    if (delta<0):
        result = 'No solution!'
    else: 
        if (delta==0):
            x1=(-numberB)/(2*numberA)
            result = 'Many solutions‚ '+str(x1)
        else:
            x1 = (-numberB-math.sqrt(delta))/(2*numberA)
            x2 = (-numberB+math.sqrt(delta))/(2*numberA)
            result = ('The equation has 2 roots '+str(x1)+' and '+str(x2))
else:
    if(numberB!=0):
        x1=-numberC/numberB
        result='The equation has only 1 root '+str(x1)
    else:
        if(numberC==0):
             result = 'To many roots'
        else:
             result = 'No solution'
print(result)
 
        
# No information about loop to make in exercise 
 
        
