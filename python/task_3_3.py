"""Task: Write a script that asks the user about:
• range of numbers to draw, e.g. "Specify the range of numbers to draw from 1 to: ..."
• number of drawn numbers, e.g. "Enter how many numbers are to be drawn from the given range."
Save the drawn numbers to the wylosowane.txt file so that each number is on its own line. After executing the script, display the information about the number of lines in the wylosowane.txt file.
Include the random library in the script for the draw.""" 

import random

fileWriter = open('wylosowane.txt','w')

a = int(input('Enter the max range of numbers from which numbers will be drawn\n'))
b = int(input('How many numbers to draw?\n'))
i=0

for liczb in range(b):
    fileWriter.write(str(random.randrange(1,a+1)) + '\n')
    i+=1

print('The program has drawn '+str(i)+' numbers in the range of 1 to '+str(a)+', which were saved in the wylosowane.txt file.')

fileWriter.close()
