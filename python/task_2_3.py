"""
Task: Write a program for calculating the real roots of a quadratic equation. The program should first read the parameters a, b, c of the quadratic equation.

DELTA=b2-4ac

if:

• DELTA<0 no solutions

• DELTA=0 one solution

• DELTA>0 two solutions

An example of the program operation:

Enter a: 1
Enter b: -4
Enter c: 4
one solution: x = 2.0

Please list the number of real solutions and solution values. You can use the math package to calculate the root.
"""

import math

number_A = int(input('Enter a: '))
number_B = int(input('Enter b: '))
number_C = int(input('Enter c: '))
if (number_A!=0):
    delta=(number_B*number_B)-(4*number_A*number_C)
    if (delta<0):
        result = 'No solution!'
    else: 
        if (delta==0):
            x1=(-number_B)/(2*number_A)
            result = 'Many solutions‚ '+str(x1)
        else:
            x1 = (-number_B-math.sqrt(delta))/(2*number_A)
            x2 = (-number_B+math.sqrt(delta))/(2*number_A)
            result = ('The equation has 2 roots '+str(x1)+' and '+str(x2))
else:
    if(number_B!=0):
        x1=-number_C/numbe_rB
        result='The equation has only 1 root '+str(x1)
    else:
        if(number_C==0):
             result = 'To many roots'
        else:
             result = 'No solution'
print(result)
