"""
Task: Sergeant Thomson decided to censor the letters his soldiers receive. This censorship involves removing every third line from the letter. Help the sergeant: write a program that receives a text file with a letter and creates its censored version - task_5_1_letter_censor.txt.

The task_5_1_letter.txt file exists before, and the task_5_1_letter_censor.txt file is created by the program.
"""
file_write = open('task_5_1_letter_censor.txt','w')
file_read = open('task_5_1_letter.txt','r')
i=1

all_lines = file_read.readlines()

for line in all_lines: #Reading all lines from a text file
    if (i==1):
        file_write.write(line)
        i+=1
    elif (i==2):
        file_write.write(line)
        i+=1
    elif (i==3):
        i+=1    
    elif (i==4):
        file_write.write(line)
        i+=1
    elif (i==5):
        file_write.write(line)
        i+=1
    elif (i==6):
        i+=1    
    elif (i==7):
        file_write.write(line)
        i+=1
    elif (i==8):
        file_write.write(line)
        i+=1
    elif (i==9):
        i+=1    
    elif (i==10):
        file_write.write(line)
        i+=1
    elif (i==11):
        file_write.write(line)
        i+=1
    elif (i==12):
        i+=1    
    elif (i==13):
        file_write.write(line)
        i+=1
    elif (i==14):
        file_write.write(line)
        i+=1     
    elif (i==15):
        i=1       
             
file_write.close()
file_read.close()

