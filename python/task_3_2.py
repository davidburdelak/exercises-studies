"""
Write a program that accepts a text file called text.txt as the input and creates a file in which the last 12 characters are repeated in each line. E.g:

File text.txt:

Czas ucieka wieczność czeka.
Kruk krukowi oka nie wykole.
Praca uszlachetnia lenistwo uszczęśliwia.

Result of script:

Czas ucieka wieczność czeka.zność czeka.
Kruk krukowi oka nie wykole.ka nie wykole.
Praca uszlachetnia lenistwo uszczęśliwia.szczęśliwia.
"""

#If u want open this file, you must create text.txt and then insert the text.

file_write = open('newText.txt','w')
file_read = open('text.txt','r')

all_lines = file_read.readlines()

for line in all_lines: #Reading all lines from a text file
    line=line.rstrip() #The rstrip statement removes the '\ n' character denoting the end of the line.
    file_write.write(line + line[-12:] +"\n")
file_write.close()
file_read.close()
