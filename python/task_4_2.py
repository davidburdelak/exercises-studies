"""
Task: Write a program to check if the given task_4_2_result.csv file - is in the correct CSV format: polea; poleb; E;
Assumptions:
• the text in each field consists of lowercase letters only
• there must be a semicolon after each field.
The program should read the file line by line and check each of these lines using a regular expression. If the line is incorrect, the program should terminate with information on which line the error is.
"""

import re

file_read = open('task_4_2_result.csv','r')

p = re.compile('[A-Za-z]*[;][A-Za-z]*[;][A-Za-z]*')
count = 0
for line in file_read:
    count+=1
    if p.findall(line):
        print("")
    else:
        print("An error was detected on the " + str(count)+ " line.")

file_read.close()        
