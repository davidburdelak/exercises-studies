"""
Task: Write a script that asks the user about:
• range of numbers to draw, e.g. "Specify the range of numbers to draw from 1 to: ..."
• number of drawn numbers, e.g. "Enter how many numbers are to be drawn from the given range."
Save the drawn numbers to the drawn.txt file so that each number is on its own line. After executing the script, display the information about the number of lines in the drawn.txt file.
Include the random library in the script for the draw.
""" 

import random

file_writer = open('drawn.txt','w')

max_range = int(input('Enter the max range of numbers from which numbers will be drawn\n'))
numbers_to_draw = int(input('How many numbers to draw?\n'))
draw_counter=0

for numbers in range(numbers_to_draw):
    file_writer.write(str(random.randrange(1,max_range+1)) + '\n')
    draw_counter+=1

print('The program has drawn '+str(draw_counter)+' numbers in the range of 1 to '+str(max_range)+', which were saved in the drawn.txt file.')

file_writer.close()
