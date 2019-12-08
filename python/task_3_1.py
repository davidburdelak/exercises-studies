"""
Task: Replace the data.txt file with the following values:

Isabella
Roberts
24
Taylor
Brown
22
James
Smith
23

to the CSV file in this form:

Isabella;Roberts;24
Taylor;Brown;22
James;Smith;23
"""

file_write = open('data.csv','w')
file_read = open('data.txt','r')
i=1

all_lines = file_read.readlines()

for line in all_lines: #Reading all lines from a text file
    if (i==1):
        line=line.rstrip() #The rstrip statement removes the '\ n' character denoting the end of the line.
        file_write.write(line+';')
        i+=1
    elif (i==2):
        line=line.rstrip()
        file_write.write(line+';')
        i+=1
    elif (i==3):
        file_write.write(line)
        i=1
file_write.close()
file_read.close()
